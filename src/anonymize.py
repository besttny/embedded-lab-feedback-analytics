import pandas as pd
import re
from pathlib import Path

RAW_FILE = Path("data/raw/feedback_raw_template.csv")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "feedback_clean.csv"

REQUIRED_COLS = ["section", "comment", "lab_no", "category"]

TEACHER_PATTERNS = [
    r"อ\.?\s*แยม",
    r"อาจารย์\s*แยม",
    r"อ\.?\s*พิชญะ",
    r"อาจารย์\s*พิชญะ",
    r"อ\.?\s*สุขุม",
    r"อาจารย์\s*สุขุม",
]

TA_PATTERNS = [
    r"TA\s*เดช",
    r"TA\s*นิค",
    r"T[Aa]\s*Dech",
    r"T[Aa]\s*Nick",
    r"พี่\s*เดช",
    r"พี่\s*นิค",
    r"\bเดช\b",
    r"\bนิค\b",
    r"\bNick\b",
    r"\bDech\b",
]


def sanitize_comment(text: str) -> str:
    """แทนชื่อจริงของอาจารย์และ TA ด้วย [REDACTED_TEACHER] / [REDACTED_TA]"""
    if not isinstance(text, str):
        return ""
    t = text.strip()
    for pat in TEACHER_PATTERNS:
        t = re.sub(pat, "[REDACTED_TEACHER]", t, flags=re.IGNORECASE)
    for pat in TA_PATTERNS:
        t = re.sub(pat, "[REDACTED_TA]", t, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", t).strip()

def replace_redacted(text: str) -> str:
    """แทน [REDACTED_*] ด้วย <Teacher> หรือ <TA>"""
    if pd.isna(text):
        return text
    text = re.sub(r"\[REDACTED_TEACHER\]", "<Teacher>", text)
    text = re.sub(r"\[REDACTED_TA\]", "<TA>", text)
    return text

def normalize_section(val: str) -> str:
    if not isinstance(val, str):
        return "Other"
    v = val.strip().lower()
    if "tim" in v:
        return "Timing"
    if "doc" in v:
        return "Document"
    if "ta" in v or "teach" in v:
        return "TA/Teacher"
    if "hard" in v or "equip" in v or "board" in v:
        return "Hardware"
    if "oth" in v:
        return "Other"
    return "Other"

def normalize_category(val: str) -> str:
    if not isinstance(val, str):
        return "general"
    v = val.strip().lower()
    mapping = {
        "time": "time",
        "timing": "time",
        "document": "document",
        "doc": "document",
        "ta": "ta",
        "equipment": "equipment",
        "equip": "equipment",
        "general": "general",
        "other": "general",
    }
    return mapping.get(v, v if v else "general")

def to_int_or_none(x):
    if pd.isna(x) or x == "":
        return None
    x_str = str(x).strip()
    # ถ้ามี comma หรือ dash → ถือว่าเป็นหลาย lab
    if "," in x_str or "-" in x_str:
        return x_str
    try:
        return int(float(x_str))
    except:
        return None

def to_str_or_none(x):
    """แปลงค่า lab_no ให้เป็น string เสมอ (หรือ None ถ้าว่าง)"""
    if pd.isna(x) or str(x).strip() == "":
        return None
    return str(x).strip()

def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw CSV not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE, encoding="utf-8")

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}. Expected {REQUIRED_COLS}")

    df.insert(0, "anon_id", [f"anon_{i:05d}" for i in range(1, len(df) + 1)])

    # Clean and Standardize
    df["section"] = df["section"].apply(normalize_section)
    df["category"] = df["category"].apply(normalize_category)
    df["lab_no"] = df["lab_no"].apply(to_str_or_none)
    df["comment"] = df["comment"].apply(sanitize_comment).apply(replace_redacted)

    for c in ["section", "category"]:
        df[c] = df[c].astype(str).str.strip()

    # จัดลำดับคอลัมน์ให้ตรงมาตรฐาน
    cols = ["anon_id", "section", "lab_no", "category", "comment"]
    df = df[cols]

    df.to_csv(OUT_FILE, index=False, encoding="utf-8-sig")
    print(f"✅ Saved → {OUT_FILE} (rows={len(df)})")

if __name__ == "__main__":
    main()
