import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="Coffee Sales Dashboard",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Coffee Sales Dashboard")

DATA_PATH = Path(__file__).parent.parent / "data" / "Coffee_sales.csv"
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])

# ───────────────────────────
# SIDEBAR FILTERS
# ───────────────────────────
st.sidebar.header("Filters")

# Date range slider
min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.slider(
    "Date range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD",
)

# Hour-of-day slider
min_hour = int(df["hour_of_day"].min())
max_hour = int(df["hour_of_day"].max())

hour_range = st.sidebar.slider(
    "Hour of day",
    min_value=min_hour,
    max_value=max_hour,
    value=(min_hour, max_hour),
    help="Filter transactions by hour of day (24-hour clock).",
)

# Coffee type checkboxes
st.sidebar.subheader("Coffee types")

coffee_types = sorted(df["coffee_name"].unique())
selected_coffees = []

for coffee in coffee_types:
    checked = st.sidebar.checkbox(coffee, value=True, key=f"coffee_{coffee}")
    if checked:
        selected_coffees.append(coffee)

# Build filtered dataframe
df_filtered = df.copy()

# Apply date filter
start_date, end_date = date_range
df_filtered = df_filtered[
    (df_filtered["Date"].dt.date >= start_date)
    & (df_filtered["Date"].dt.date <= end_date)
]

# Apply hour-of-day filter
start_hour, end_hour = hour_range
df_filtered = df_filtered[
    (df_filtered["hour_of_day"] >= start_hour)
    & (df_filtered["hour_of_day"] <= end_hour)
]

# Apply coffee type filter
if selected_coffees:
    df_filtered = df_filtered[df_filtered["coffee_name"].isin(selected_coffees)]
else:
    # If nothing is selected, keep an empty frame
    df_filtered = df_filtered.iloc[0:0]

# ───────────────────────────
# ROW 1
# ───────────────────────────
col1_r1, col2_r1, col3_r1 = st.columns(3)

with col1_r1:
    st.subheader("Row 1 — Column 1")
    st.write("Placeholder for KPI or summary element.")

with col2_r1:
    st.subheader("Row 1 — Column 2")
    st.write("Placeholder for KPI or summary element.")

with col3_r1:
    st.subheader("Row 1 — Column 3")
    st.write("Placeholder for KPI or summary element.")


# ───────────────────────────
# ROW 2
# ───────────────────────────
big_col_r2, col3_r2 = st.columns([2, 1])

with big_col_r2:
    st.subheader("Row 2 — Columns 1 & 2")
    st.write("Placeholder for primary dashboard chart.")

with col3_r2:
    st.subheader("Row 2 — Column 3")
    st.write("Placeholder for insights or explanation.")


# ───────────────────────────
# ROW 3
# ───────────────────────────
col1_r3, col2_r3, col3_r3 = st.columns(3)

with col1_r3:
    st.subheader("Row 3 — Column 1")
    st.write("Placeholder for chart.")

with col2_r3:
    st.subheader("Row 3 — Column 2")
    st.write("Placeholder for chart.")

with col3_r3:
    st.subheader("Row 3 — Column 3")
    st.write("Placeholder for chart.")


# ───────────────────────────
# ROW 4
# ───────────────────────────
col1_r4, col2_r4, col3_r4 = st.columns(3)

with col1_r4:
    st.subheader("Row 4 — Column 1")
    st.write("Placeholder for explanation text.")

with col2_r4:
    st.subheader("Row 4 — Column 2")
    st.write("Placeholder for explanation text.")

with col3_r4:
    st.subheader("Row 4 — Column 3")
    st.write("Placeholder for explanation text.")


# ───────────────────────────
# FOOTER
# ───────────────────────────
st.divider()
st.caption("Footer text or data source reference goes here.")
