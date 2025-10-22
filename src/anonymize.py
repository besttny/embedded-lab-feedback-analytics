import pandas as pd
import re
from pathlib import Path

RAW_FILE = Path("data/raw/feedback_raw_template.csv")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "feedback_clean.csv"

REQUIRED_COLS = ["section", "comment", "lab_no", "category"]

SENSITIVE_PATTERNS = [
    r"(อ\.|อาจารย์)\s+(?!ไม่|ควร|พูด|ดุ|สอน|ยัง|ขาด|สอนน้อย|เข้ม|ใจดี|ใจร้าย|เลย|โอ|โอเค)[ก-๙A-Za-z]{2,}",
    r"[A-Za-zก-๙]+(?:\s+[A-Za-zก-๙]+){0,2}\s*(?:สอนไม่ดี|พูดเร็ว|ดุ)",
    r"\b66\d{8}\b",
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
]

def sanitize_comment(text: str) -> str:
    if not isinstance(text, str):
        return ""
    t = text.strip()
    for pat in SENSITIVE_PATTERNS:
        t = re.sub(pat, "[REDACTED]", t, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", t)

def normalize_section(val: str) -> str:
    if not isinstance(val, str):
        return "Other"
    v = val.strip().lower()
    if "tim" in v:
        return "Timing"
    if "doc" in v:
        return "Document"
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

def replace_redacted(text):
    if pd.isna(text):
        return text
    # <TA>
    text = re.sub(r"\[REDACTED\]\s*([Tt][Aa]|ทีเอ)", "<TA>", text)
    # <Teacher>
    text = re.sub(r"\[REDACTED\]\s*[้\s]*(สอน|อาจารย์|teacher)", "<Teacher>", text)
    return text

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
