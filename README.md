# Embedded Lab Feedback Analytics

A mini data project analyzing student feedback from the Embedded Systems Laboratory course.
This project demonstrates the complete data pipeline from **ETL** to **analysis** and **visualization**, with components from **Data Engineering**, **Data Analysis**, and **Data Science**.

---

## 📂 Project Structure
data/
├── raw/ # original survey or feedback files
├── interim/ # cleaned but not yet finalized
└── processed/ # ready-to-analyze datasets

db/
├── schema.sql # table schema
└── sample_queries.sql # example SQL queries

notebooks/
├── 01_extract_clean.ipynb # cleaning and transformation
└── 02_eda.ipynb # exploration and visualization

src/
├── etl_load.py # ETL to PostgreSQL
└── anonymize.py # anonymization logic

dashboard/
└── app.py # Streamlit / Plotly dashboard

docs/
├── data_dictionary.md
└── ethics_disclaimer.md

---

## 🎯 Project Objectives
- Build an ETL pipeline to clean and load feedback data into a SQL database.
- Perform exploratory data analysis (EDA) to find trends and correlations.
- Visualize results through an interactive dashboard.
- Apply simple sentiment or regression models for further insights.

---

## 🧰 Tech Stack
- **Python** (pandas, matplotlib, seaborn, plotly, scikit-learn)
- **SQL** (PostgreSQL)
- **Streamlit** or **Plotly Dash** for visualization
- **GitHub** for version control and portfolio presentation

---

## ⚙️ Workflow Timeline
| Phase | Description | Output |
|:--|:--|:--|
| Day 1–2 | Data Cleaning & Anonymization | `feedback_clean.csv` |
| Day 3 | Database Setup & ETL | `schema.sql`, loaded DB |
| Day 4–5 | EDA & Visualization | graphs, insights |
| Day 6 | Dashboard Development | Streamlit app |
| Day 7 | Modeling (optional) & Final Report | regression/sentiment results |

---

## 🛡️ Data Ethics
This dataset has been **anonymized** and is used **solely for educational and portfolio purposes**.

---

## 📈 Example Insights (to be added)
- Average satisfaction per lab and section  
- Correlation between TA helpfulness and overall score  
- Sentiment distribution in open comments  

---

## 👨‍💻 Author
Thanayot Chalernpornlert  
Computer Engineering Student @ Chulalongkorn University  