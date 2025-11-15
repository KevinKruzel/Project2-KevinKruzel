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


# ───────────────────────────
# SIDEBAR FILTERS (Placeholder Only)
# ───────────────────────────
st.sidebar.header("Filters")
st.sidebar.write("Sidebar filter controls will go here.")
st.sidebar.write("Example: date range, coffee type, weekday, time of day, etc.")


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
