import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Load new dataset
DATA_PATH = Path(__file__).parent.parent / "data" / "Coffee_sales.csv"
df = pd.read_csv(DATA_PATH)

st.set_page_config(
    page_title="Coffee Sales EDA Gallery",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Coffee Sales EDA Gallery")

# ───────────────────────────
# ROW 1
# ───────────────────────────
big_col_r1, col3_r1 = st.columns([2, 1])

with big_col_r1:
    df["Date"] = pd.to_datetime(df["Date"])

    daily_sales = df.groupby(df["Date"].dt.date)["money"].sum().reset_index()
    daily_sales.columns = ["Date", "Total_Revenue"]

    fig = px.line(
        daily_sales,
        x="Date",
        y="Total_Revenue",
        title="Daily Coffee Revenue Over Time",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Revenue ($)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

with col3_r1:
    st.subheader("Row 1 — Column 3")
    st.write("Placeholder content to be filled later.")

# ───────────────────────────
# ROW 2
# ───────────────────────────
col1_r2, col2_r2, col3_r2 = st.columns(3)

with col1_r2:
    st.subheader("Row 2 — Column 1")
    st.write("Placeholder content to be filled later.")

with col2_r2:
    st.subheader("Row 2 — Column 2")
    st.write("Placeholder content to be filled later.")

with col3_r2:
    st.subheader("Row 2 — Column 3")
    st.write("Placeholder content to be filled later.")

# ───────────────────────────
# ROW 3
# ───────────────────────────
col1_r3, col2_r3, col3_r3 = st.columns(3)

with col1_r3:
    st.subheader("Row 3 — Column 1")
    st.write("Placeholder content to be filled later.")

with col2_r3:
    st.subheader("Row 3 — Column 2")
    st.write("Placeholder content to be filled later.")

with col3_r3:
    st.subheader("Row 3 — Column 3")
    st.write("Placeholder content to be filled later.")

st.divider()

# Footer
st.caption("**Data source:** https://www.kaggle.com/datasets/kainatjamil12/coffe-sale/data")

with st.expander("Data Preview"):
    st.dataframe(df)

# Read the CSV file for download
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Raw Data (CSV)",
    data=csv_data,
    file_name="Coffee_sales.csv",
    mime="text/csv",
)
