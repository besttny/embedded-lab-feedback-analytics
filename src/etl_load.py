import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_USER = os.getenv("PG_USER", "postgres")
PG_PASSWORD = os.getenv("PG_PASSWORD", "")
PG_DATABASE = os.getenv("PG_DATABASE", "feedbackdb")

CSV_PATH = Path("data/processed/feedback_clean.csv")
SCHEMA_PATH = Path("db/schema.sql")

def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"❌ Processed CSV not found: {CSV_PATH}")

    print(f"Loading data from {CSV_PATH} ...")
    df = pd.read_csv(CSV_PATH, encoding="utf-8-sig")

    # Create SQLAlchemy connection URL
    conn_url = (
        f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
    )
    engine = create_engine(conn_url)

    with engine.connect() as conn:
        # Create table from schema.sql
        if SCHEMA_PATH.exists():
            schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
            conn.execute(text(schema_sql))
            conn.commit()
            print("Table was created (from schema.sql)")
        else:
            print("schema.sql not found, skipping table creation")

        # Insert data
        print(f"Inserting {len(df)} rows into 'feedback' ...")
        df.to_sql("feedback", con=engine, if_exists="append", index=False)
        print("Data successfully loaded!")

if __name__ == "__main__":
    main()
