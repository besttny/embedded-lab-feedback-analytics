# 🧩 Embedded Lab Feedback Analytics

A mini data project analyzing student feedback from the **Embedded Systems Laboratory** course.  
This project demonstrates the complete data pipeline from **ETL** to **analysis** and **visualization**,  
covering **Data Engineering**, **Data Analysis**, and **Data Science** components.

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
- *(Optional)* Apply sentiment or feature importance analysis for deeper insights.

---

## 🧰 Tech Stack
- **Python** → pandas, matplotlib, seaborn, plotly, scikit-learn  
- **SQL** → PostgreSQL  
- **Visualization** → Streamlit / Plotly Dash  
- **Version Control** → GitHub  

---

## 🗓️ Timeline (MVP)
| Day | Task | Output |
|:--:|:--|:--|
| 1–2 | Cleaning & anonymization | `data/processed/feedback_clean.csv` |
| 3 | DB schema & ETL | PostgreSQL database |
| 4–5 | EDA & key visualizations | insights + graphs |
| 6 | Streamlit dashboard | interactive web app |
| 7 | *(Optional)* sentiment / feature importance | analytical report |

---

## 🛡️ Data Ethics
This dataset has been **fully anonymized** and is used **solely for educational and portfolio purposes**.  
No personally identifiable information (PII) is included.

---

## 📈 Example Insights (to be added)
- Average satisfaction per lab and section  
- Correlation between TA helpfulness and overall score  
- Sentiment distribution in open comments  

---

## 👨‍💻 Author
**Thanayot Chalernpornlert**  
Computer Engineering Student @ Chulalongkorn University  
📧 *[your.email@example.com]* | 🌐 [github.com/yourusername](https://github.com/yourusername)
