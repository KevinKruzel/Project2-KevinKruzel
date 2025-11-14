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
    st.subheader("Daily Coffee Revenue Over Time")
    df["Date"] = pd.to_datetime(df["Date"])

    daily_sales = (
        df.groupby(df["Date"].dt.date)["money"]
        .sum()
        .reset_index()
        .rename(columns={"Date": "Date", "money": "Total_Revenue"})
    )

    chart_placeholder = st.empty()
    slider_placeholder = st.empty()

    min_date = daily_sales["Date"].min()
    max_date = daily_sales["Date"].max()

    start_date, end_date = slider_placeholder.slider(
        "Select date range to display",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
        format="YYYY-MM-DD",
    )

    mask = (daily_sales["Date"] >= start_date) & (daily_sales["Date"] <= end_date)
    filtered_sales = daily_sales[mask]

    fig = px.line(
        filtered_sales,
        x="Date",
        y="Total_Revenue",
        markers=True,
        title=""
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Revenue ($)",
        hovermode="x unified",
        margin=dict(l=10, r=10, t=40, b=10),
    )

    chart_placeholder.plotly_chart(fig, use_container_width=True)

with col3_r1:
    st.markdown("""
**What question is this chart exploring?**  
*How does total coffee revenue change over time?*

**How to read this chart**
- The x-axis represents calendar dates.
- The y-axis shows the total revenue earned from coffee sales on each day.
- Each point represents a full day of revenue.
- Use the slider below the chart to zoom into a specific date range (for example, one week or a month).

**Insights from the data**
- Revenue fluctuates very noticeably between days, indicating natural peaks and slower periods.
- Some days show significantly higher revenue, suggesting busy or high-traffic days.
- There are also occasional dips that stand out compared to surrounding days.
- The interactive slider makes it clear that variability exists even within small time windows.
    """)

# ───────────────────────────
# ROW 2
# ───────────────────────────
col1_r2, col2_r2, col3_r2 = st.columns(3)

with col1_r2:
    coffee_counts = df["coffee_name"].value_counts().reset_index()
    coffee_counts.columns = ["Coffee_Type", "Count"]

    fig = px.pie(
        coffee_counts,
        names="Coffee_Type",
        values="Count",
        title="Distribution of Coffee Types Sold",
        hole=0.3  # donut style; remove if you want full pie
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2_r2:
    weekday_sales = df.groupby(["Weekday", "Weekdaysort"])["money"].sum().reset_index()
    weekday_sales = weekday_sales.sort_values("Weekdaysort")  # ensures correct order

    fig = px.bar(
        weekday_sales,
        x="Weekday",
        y="money",
        title="Total Revenue by Weekday",
        text_auto=True,
    )

    fig.update_layout(
        xaxis_title="Day of Week",
        yaxis_title="Total Revenue ($)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

with col3_r2:
    fig = px.histogram(
        df,
        x="hour_of_day",
        nbins=24,  # one bin per hour
        title="Sales Activity by Time of Day",
    )

    fig.update_layout(
        xaxis_title="Hour of Day (24-hour format)",
        yaxis_title="Number of Sales",
        bargap=0.05
    )

    st.plotly_chart(fig, use_container_width=True)

# ───────────────────────────
# ROW 3
# ───────────────────────────
col1_r3, col2_r3, col3_r3 = st.columns(3)

with col1_r3:
    st.markdown("""
**What question is this chart exploring?**  
*What is the proportion of each type of coffee being sold?*

**How to read this chart**
- Each slice represents one type of coffee beverage that the store sells.
- The size of the slice shows the proportion of total transactions belonging to that drink.
- Percentage labels show how large each category is relative to the whole.
- Hovering over the slices of the pie displays the exact count values.

**Insights from the data**
- Some drinks are significantly more popular than others, making up a larger share of purchases.
- A relatively small number of coffee types account for a majority of the total sales.
- Smaller slices represent drinks bought less often.
- The distribution highlights possible customer drink preferences.
    """)

with col2_r3:
    st.markdown("""
**What question is this chart exploring?**  
*Which days of the week generate the most sales revenue?*

**How to read this chart**
- The x-axis shows each weekday (Monday–Sunday).
- The height of each bar represents total revenue earned that day.
- Taller bars mean more sales occurred on that day.
- Numeric labels make comparison easier.

**Insights from the data**
- Certain days on average generate more revenue than others.
- The highest bars indicate the busiest days of the week for the business, most notably the weekdays.
- Slower days stand out clearly, most notably the weekends, and may represent less shop activity.
- The pattern suggests predictable weekly sales cycles.
    """)

with col3_r3:
    st.markdown("""
**What question is this chart exploring?**  
*What times of day have the highest sales activity?*

**How to read this chart**
- The x-axis shows the hour of day using a 24-hour clock (6 is 6 AM, 12 is Noon, 18 is 6 PM, etc.).
- The height of each bar indicates how many transactions occurred within that hour.
- Peaks show high-demand time windows and valleys show slower periods.
- Each bar covers eactly a one hour time frame.

**Insights from the data**
- Sales tend to cluster around certain daily time periods, most notably the mornings and evenings.
- Morning hours appear to be significantly busier than late afternoon or evening.
- Overnight or early-morning hours comparatively less activity.
- The chart reveals strong daily purchasing patterns aligned with coffee consumption habits.
    """)

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
