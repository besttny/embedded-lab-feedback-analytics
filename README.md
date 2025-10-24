# 🧩 Embedded Lab Feedback Analytics

A mini data project analyzing student feedback from the **Embedded Systems Laboratory** course at Chulalongkorn University.  
This project demonstrates the full data pipeline from **data extraction, anonymization, and ETL**, through **analysis** and **visualization**,  
covering **Data Engineering**, **Data Analysis**, and **Data Science** components.

---

## 📂 Project Structure

```
data/
├── raw/ # original survey or feedback files
├── interim/ # cleaned but not yet finalized
└── processed/ # ready-to-analyze datasets

db/
├── schema.sql # table schema
└── sample_queries.sql # example SQL queries

notebooks/
├── 01_extract_clean.ipynb # cleaning and transformation
├── 02_eda.ipynb # exploration and visualization
└── 03_advanced_analytics.ipynb # Sentiment + Word Cloud + Insights

src/
├── anonymize.py # anonymization logic for names and TA references
├── etl_load.py # ETL pipeline to load data into PostgreSQL
└── sentiment_analysis.py # keyword or model-based sentiment module

dashboard/
└── app.py # Streamlit / Plotly dashboard

docs/
├── data_dictionary.md
└── ethics_disclaimer.md
```

---

## 🎯 Project Objectives
- Build a reproducible **ETL pipeline** to clean and load feedback data into PostgreSQL  
- Perform **exploratory data analysis (EDA)** to uncover trends and patterns  
- Conduct **sentiment analysis** on open-ended comments (Thai + English)  
- Visualize insights interactively via a **Streamlit dashboard**  
- Apply data ethics and anonymization best practices  

---

## 🧰 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3.13, SQL |
| **Data Handling** | pandas, numpy, re |
| **Visualization** | matplotlib, seaborn, wordcloud |
| **Database** | PostgreSQL + SQLAlchemy |
| **Text Analysis** | PyThaiNLP *(or simple keyword-based sentiment)* |
| **App / Dashboard** | Streamlit / Plotly Dash |
| **Env Management** | dotenv (.env) |
| **Version Control** | Git + GitHub |

---

## 🗓️ Timeline (MVP)
| Day | Phase | เป้าหมายหลัก | ผลลัพธ์ที่ได้ |
|:--:|:--|:--|:--|
| **Day 0** | 🔧 Setup & Planning | สร้าง repo, README, ethics disclaimer, โครงสร้าง project | โครงสร้าง repo พร้อมใช้งาน |
| **Day 1** | 🧹 Data Extraction & Cleaning | แปลง feedback PDF → CSV และ clean ข้อความ | `feedback_raw.csv` |
| **Day 2** | 🛡️ Anonymization & ETL | ลบชื่อ อาจารย์ / TA ด้วย `anonymize.py` และ โหลดเข้า DB | `feedback_clean.csv` + ตาราง `feedback` ใน PostgreSQL |
| **Day 3** | 📊 Database Validation & EDA | ตรวจสอบ schema, query, และ ทำ EDA ด้วย SQL + Python | กราฟ และ สรุป ข้อมูล เบื้องต้น |
| **Day 4** | 🧠 Sentiment & Advanced Analytics | วิเคราะห์ อารมณ์ (pos / neu / neg) + Word Cloud และ Top Keywords | `feedback_sentiment.csv` + กราฟ เชิงลึก |
| **Day 5** | 📈 Dashboard Development | สร้าง Streamlit dashboard พร้อม filter และ กราฟ interactive | `dashboard/app.py` |
| **Day 6** | 🎨 Storytelling & Insight Design | ปรับ layout, สรุป key insights, เตรียม presentation | Final graphs + storyboard |
| **Day 7** | 🚀 Final Report & Portfolio Prep | เขียน README สรุปผล และ เตรียม portfolio | Repo พร้อม showcase ใน GitHub / Resume |

---

## 🛡️ Data Ethics
This dataset has been **fully anonymized** and is used **solely for educational and portfolio purposes**.  
No personally identifiable information (PII) such as names, emails, or student IDs is included.  

📄 See: [`docs/ethics_disclaimer.md`](docs/ethics_disclaimer.md)

---

## 📈 Example Insights (to be added)
- Average satisfaction by lab section (time vs difficulty)  
- Clarity of documentation correlates with neutral sentiments  
- TA availability affects overall feedback tone  
- Common phrases: “เวลา”, “doc”, “TA”, “ไม่เข้าใจ”

---

## 👨‍💻 Author
**Thanayot Chalernpornlert**  
Computer Engineering Student @ Chulalongkorn University  
📧 *[thanayot.47@gmail.com]* | 🌐 [github.com/besttny]