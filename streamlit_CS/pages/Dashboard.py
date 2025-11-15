import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

COFFEE_CONTINUOUS = ["#F7F3EE", "#D2B48C", "#C19A6B", "#A47148", "#6F4E37", "#3B2F2F"]

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

start_date, end_date = date_range
df_filtered = df_filtered[
    (df_filtered["Date"].dt.date >= start_date)
    & (df_filtered["Date"].dt.date <= end_date)
]

start_hour, end_hour = hour_range
df_filtered = df_filtered[
    (df_filtered["hour_of_day"] >= start_hour)
    & (df_filtered["hour_of_day"] <= end_hour)
]

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
    st.subheader("Sales Heatmap by Day and Hour")

    if df_filtered.empty:
        st.warning("No data available for the selected filters.")
    else:
        heatmap_data = (
            df_filtered.groupby(["Weekday", "Weekdaysort", "hour_of_day"])["money"]
            .sum()
            .reset_index()
        )

        weekday_order = (
            heatmap_data[["Weekday", "Weekdaysort"]]
            .drop_duplicates()
            .sort_values("Weekdaysort")["Weekday"]
            .tolist()
        )

        pivot_table = heatmap_data.pivot_table(
            index="Weekday",
            columns="hour_of_day",
            values="money",
            fill_value=0
        )

        pivot_table = pivot_table.reindex(index=weekday_order)

        pivot_table = pivot_table[sorted(pivot_table.columns)]

        fig = px.imshow(
            pivot_table,
            text_auto=True,
            aspect="auto",
            color_continuous_scale=COFFEE_CONTINUOUS,
            labels=dict(color="Total Revenue ($)")
        )

        fig.update_layout(
            xaxis_title="Hour of Day (24-hour clock)",
            yaxis_title="Day of Week",
            margin=dict(l=10, r=10, t=40, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)

with col3_r2:
    st.subheader("Row 2 — Column 3")
    st.write("Placeholder for insights or explanation.")

# ───────────────────────────
# ROW 3
# ───────────────────────────
col1_r3, col2_r3, col3_r3 = st.columns(3)

with col1_r3:
    st.subheader("Revenue by Coffee Type")

    if df_filtered.empty:
        st.warning("No data available for the selected filters.")
    else:
        # Aggregate revenue by coffee type
        coffee_revenue = (
            df_filtered.groupby("coffee_name")["money"]
            .sum()
            .reset_index()
            .sort_values("money", ascending=False)
        )

        fig = px.bar(
            coffee_revenue,
            x="coffee_name",
            y="money",
            title="Total Revenue by Coffee Type",
            text_auto=True,
            color_discrete_sequence=["#6F4E37"]
        )

        fig.update_layout(
            xaxis_title="Coffee Type",
            yaxis_title="Total Revenue ($)",
            margin=dict(l=10, r=10, t=40, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)

with col2_r3:
    st.subheader("Distribution of Sale Times by Month")

    if df_filtered.empty:
        st.warning("No data available for the selected filters.")
    else:
        month_order = (
            df_filtered[["Month_name", "Monthsort"]]
            .drop_duplicates()
            .sort_values("Monthsort")["Month_name"]
            .tolist()
        )

        fig = px.box(
            df_filtered,
            x="Month_name",
            y="hour_of_day",
            category_orders={"Month_name": month_order},
            title="Hourly Sale Time Distribution by Month",
            color_discrete_sequence=["#8B5A2B"],  # coffee brown
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Hour of Day (24-hour clock)",
            margin=dict(l=10, r=10, t=40, b=10),
        )

        fig.update_yaxes(range=[0, 23], dtick=2)

        st.plotly_chart(fig, use_container_width=True)
with col3_r3:
    st.subheader("Total Revenue by Month")

    if df_filtered.empty:
        st.warning("No data available for the selected filters.")
    else:
        monthly_revenue = (
            df_filtered.groupby(["Month_name", "Monthsort"])["money"]
            .sum()
            .reset_index()
            .rename(columns={"money": "total_revenue"})
            .sort_values("Monthsort")
        )

        month_order = (
            monthly_revenue[["Month_name", "Monthsort"]]
            .drop_duplicates()
            .sort_values("Monthsort")["Month_name"]
            .tolist()
        )

        fig = px.bar(
            monthly_revenue,
            x="Month_name",
            y="total_revenue",
            title="Total Revenue by Month",
            text_auto=True,
            category_orders={"Month_name": month_order},
            color_discrete_sequence=["#A47148"]
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Total Revenue ($)",
            margin=dict(l=10, r=10, t=40, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)


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
