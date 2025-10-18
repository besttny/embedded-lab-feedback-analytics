import pandas as pd
import re
from pathlib import Path

RAW_FILE = Path("data/raw/feedback_raw_template.csv")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "feedback_clean.csv"

REQUIRED_COLS = ["section", "comment", "lab_no", "category"]

SENSITIVE_PATTERNS = [
    r"(อ\.|อาจารย์)\S+",          # ชื่ออาจารย์ติดกัน เช่น "อ.สมชาย"
    r"[A-Za-zก-๙]+(?:\s+[A-Za-zก-๙]+){0,2}\s*(?:สอนไม่ดี|พูดเร็ว|ดุ)",  # ชื่อ+คำบ่น (คร่าวๆ)
    r"\b66\d{8}\b",                 # รูปรหัสนิสิตประมาณ 10 หลักขึ้นต้นด้วย 66
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",  # อีเมล
]

def sanitize_comment(text: str) -> str:
    """ลบ/แทนที่ข้อมูลอ่อนไหวในคอมเมนต์ให้อ่านได้แต่ไม่ระบุตัวตน"""
    if not isinstance(text, str):
      return ""
    t = text.strip()
    for pat in SENSITIVE_PATTERNS:
        t = re.sub(pat, "[REDACTED]", t, flags=re.IGNORECASE)
    # เก็บแค่ช่องว่างเดียว
    t = re.sub(r"\s+", " ", t)
    return t

def normalize_section(val: str) -> str:
    if not isinstance(val, str):
        return "Other"
    v = val.strip().lower()
    if "tim" in v:      # timing
        return "Timing"
    if "doc" in v:      # document
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
    try:
        if pd.isna(x) or x == "":
            return None
        return int(float(x))
    except:
        return None

def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw CSV not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE, dtype=str).fillna("")

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}. Expected {REQUIRED_COLS}")

    df.insert(0, "anon_id", [f"anon_{i:05d}" for i in range(1, len(df) + 1)])

    # Clean and Standardize
    df["section"] = df["section"].apply(normalize_section)
    df["category"] = df["category"].apply(normalize_category)
    df["lab_no"] = df["lab_no"].apply(to_int_or_none)
    df["comment"] = df["comment"].apply(sanitize_comment)

    for c in ["section", "category"]:
        df[c] = df[c].astype(str).str.strip()

    cols = ["anon_id", "section", "lab_no", "category", "comment"]
    df = df[cols]

    df.to_csv(OUT_FILE, index=False, encoding="utf-8-sig")
    print(f"Saved → {OUT_FILE}  (rows={len(df)})")

if __name__ == "__main__":
    main()
