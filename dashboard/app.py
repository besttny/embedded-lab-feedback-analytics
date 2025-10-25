# =============================
# Embedded Feedback Dashboard
# =============================
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("../data/processed/feedback_sentiment.csv")
    return df

df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🧭 Filters")
sections = st.sidebar.multiselect(
    "เลือก Section:",
    options=df["section"].unique(),
    default=df["section"].unique()
)

categories = st.sidebar.multiselect(
    "เลือก Category:",
    options=df["category"].unique(),
    default=df["category"].unique()
)

filtered_df = df[
    (df["section"].isin(sections)) &
    (df["category"].isin(categories))
]

# -----------------------------
# Main Title
# -----------------------------
st.title("📊 Embedded Lab Feedback Dashboard")
st.markdown("วิเคราะห์ความคิดเห็นของนิสิตต่อวิชา **Embedded Systems Laboratory**")

st.info(f"จำนวน feedback ทั้งหมดที่เลือก: **{len(filtered_df)}** ข้อ")

# -----------------------------
# Sentiment Overview
# -----------------------------
st.subheader("💬 Sentiment Distribution")
sent_count = filtered_df["sentiment"].value_counts().reset_index()
sent_count.columns = ["sentiment", "count"]

fig = px.pie(
    sent_count,
    values="count",
    names="sentiment",
    color="sentiment",
    color_discrete_map={"pos": "green", "neu": "gray", "neg": "red"},
    title="Sentiment Breakdown"
)
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Category Distribution
# -----------------------------
st.subheader("📚 Feedback by Category")
cat_count = filtered_df["category"].value_counts().reset_index()
cat_count.columns = ["category", "count"]

fig2 = px.bar(
    cat_count,
    x="category", y="count",
    text_auto=True,
    color="category",
    title="จำนวน Feedback ต่อหมวดหมู่"
)
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Table View
# -----------------------------
st.subheader("🧾 Feedback Table")
st.dataframe(
    filtered_df[["section", "category", "comment", "sentiment"]],
    use_container_width=True
)
