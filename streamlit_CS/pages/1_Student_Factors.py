import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Get the absolute path to the data file relative to this script
DATA_PATH = Path(__file__).parent.parent / "data" / "StudentPerformanceFactors.csv"
df = pd.read_csv(DATA_PATH)

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

# Color theme definitions
COLOR_THEMES = {
    "Ocean Blue": {
        "scatter_primary": "#1f77b4",
        "scatter_secondary": "#ff7f0e",
        "heatmap": "Blues",
        "pie_colors": {"Yes": "#2E86AB", "High": "#2E86AB", "No": "#A23B72", "Low": "#A23B72", "Medium": "#F18F01"}
    },
    "Sunset Warm": {
        "scatter_primary": "#e74c3c",
        "scatter_secondary": "#f39c12",
        "heatmap": "YlOrRd",
        "pie_colors": {"Yes": "#e67e22", "High": "#e67e22", "No": "#c0392b", "Low": "#c0392b", "Medium": "#f39c12"}
    },
    "Forest Green": {
        "scatter_primary": "#27ae60",
        "scatter_secondary": "#16a085",
        "heatmap": "Greens",
        "pie_colors": {"Yes": "#27ae60", "High": "#27ae60", "No": "#e74c3c", "Low": "#e74c3c", "Medium": "#f39c12"}
    },
    "Purple Haze": {
        "scatter_primary": "#9b59b6",
        "scatter_secondary": "#8e44ad",
        "heatmap": "Purples",
        "pie_colors": {"Yes": "#9b59b6", "High": "#9b59b6", "No": "#e74c3c", "Low": "#e74c3c", "Medium": "#f39c12"}
    },
    "Teal Mint": {
        "scatter_primary": "#16a085",
        "scatter_secondary": "#1abc9c",
        "heatmap": "YlGnBu",
        "pie_colors": {"Yes": "#1abc9c", "High": "#1abc9c", "No": "#e74c3c", "Low": "#e74c3c", "Medium": "#f39c12"}
    },
    "Classic": {
        "scatter_primary": "#3498db",
        "scatter_secondary": "#e74c3c",
        "heatmap": "viridis",
        "pie_colors": {"Yes": "green", "High": "green", "No": "red", "Low": "red", "Medium": "yellow"}
    }
}

# Sidebar controls
st.sidebar.header("🎨 Visualization Settings")
color_theme = st.sidebar.selectbox(
    "Color Theme",
    options=list(COLOR_THEMES.keys()),
    index=0
)
theme = COLOR_THEMES[color_theme]

st.sidebar.divider()
st.sidebar.header("📊 Data Filters")
st.sidebar.caption("Filter the dataset to analyze specific student groups")

# Check if reset was requested and clear filter keys before widgets are created
if st.session_state.get("reset_filters", False):
    for key in ["gender_filter", "family_filter", "school_filter", "attendance_filter"]:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state.reset_filters = False

gender_choice = st.sidebar.selectbox("Gender", ["All", "Male", "Female"], key="gender_filter")
family_choice = st.sidebar.selectbox("Family Income", ["All", "Low", "Medium", "High"], key="family_filter")
school_choice = st.sidebar.selectbox("School Type", ["All", "Public", "Private"], key="school_filter")
att_range = st.sidebar.slider("Attendance (%)", 60, 100, (60, 100), step=1, key="attendance_filter")

# Reset button
if st.sidebar.button("🔄 Reset All Filters", use_container_width=True):
    # Set flag to reset on next rerun
    st.session_state.reset_filters = True
    st.rerun()

df_filtered = df.copy()
if gender_choice != "All":
    df_filtered = df_filtered[df_filtered["Gender"] == gender_choice]
if family_choice != "All":
    df_filtered = df_filtered[df_filtered["Family_Income"] == family_choice]
if school_choice != "All":
    df_filtered = df_filtered[df_filtered["School_Type"] == school_choice]
att_min, att_max = att_range
df_filtered = df_filtered[
    pd.to_numeric(df_filtered["Attendance"], errors="coerce").between(att_min, att_max)
]

## Make collapse for dataframe
# with st.expander("Data"):
#     st.dataframe(df_filtered)

st.title("Student Performance Factors")
# ROW 1: 
col1_r1, col2_r1 = st.columns([2, 1])

with col1_r1:
    st.subheader("Hours Studied Vs Exam Score")
    st.caption("Scatter plot + trendline")

    # graph
    x_col, y_col = "Hours_Studied", "Exam_Score"
    if x_col in df_filtered.columns and y_col in df_filtered.columns:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.scatter(df_filtered[x_col], df_filtered[y_col], alpha=0.6, color=theme["scatter_primary"])
        
        # Add trendline
        z = np.polyfit(df_filtered[x_col], df_filtered[y_col], 1)
        p = np.poly1d(z)
        ax.plot(df_filtered[x_col], p(df_filtered[x_col]), "--", alpha=0.8, linewidth=2, color=theme["scatter_secondary"])
        
        ax.set_xlabel("Hours Studied")
        ax.set_ylabel("Exam Score")
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()
    else:
        st.error('Column names not found in dataframe.')

with col2_r1:
    st.subheader("Correlation Between Study Time and Exam Scores")
    st.write("From the scatterplot it is clear there is a strong positive correlation between a student's study time and their resulting exam score. Students who put it the effort to study for long hours are likely to receive high remarks on their grades.")

# ROW 2:
col1_r2, col2_r2, col3_r2 = st.columns(3)

with col1_r2:
    st.subheader("Physical Activity Vs Exam Score")
    
    # Create bins for physical activity and exam scores
    if 'Physical_Activity' in df_filtered.columns and 'Exam_Score' in df_filtered.columns:
        # Create a pivot table for the heatmap
        activity_bins = pd.cut(df_filtered['Physical_Activity'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
        score_bins = pd.cut(df_filtered['Exam_Score'], bins=5, labels=['60-68', '68-76', '76-84', '84-92', '92-100'])
        
        heatmap_data = pd.crosstab(score_bins, activity_bins)
        
        fig, ax = plt.subplots(figsize=(6, 5))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap=theme["heatmap"], ax=ax, cbar_kws={'label': 'Count'})
        ax.set_xlabel('Physical Activity (hours/week)')
        ax.set_ylabel('Exam Score Range')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    else:
        st.error('Required columns not found.')

with col2_r2:
    st.subheader("Key Insights")
    
    # Calculate correlations and statistics
    if 'Physical_Activity' in df_filtered.columns and 'Sleep_Hours' in df_filtered.columns and 'Exam_Score' in df_filtered.columns:
        activity_corr = df_filtered['Physical_Activity'].corr(df_filtered['Exam_Score'])
        sleep_corr = df_filtered['Sleep_Hours'].corr(df_filtered['Exam_Score'])
        
        avg_activity = df_filtered['Physical_Activity'].mean()
        avg_sleep = df_filtered['Sleep_Hours'].mean()
        avg_score = df_filtered['Exam_Score'].mean()
        
        st.write(f"**Physical Activity Correlation:** {activity_corr:.3f}")
        st.write(f"**Sleep Hours Correlation:** {sleep_corr:.3f}")
        st.write("")
        st.write(f"Students average **{avg_activity:.1f} hours/week** of physical activity and **{avg_sleep:.1f} hours** of sleep per night, with an average exam score of **{avg_score:.1f}**.")
        st.write("")
        
        # Key findings based on data analysis
        st.write("➡️ Physical activity shows **minimal correlation** with exam scores.")
        st.write("")
        st.write("➡️ Sleep hours show **minimal correlation** with exam scores.")

with col3_r2:
    st.subheader("Sleep Hours Vs Exam Score")
    
    # Create bins for sleep hours and exam scores
    if 'Sleep_Hours' in df_filtered.columns and 'Exam_Score' in df_filtered.columns:
        # Create a pivot table for the heatmap
        sleep_bins = pd.cut(df_filtered['Sleep_Hours'], bins=5, labels=['4-5h', '5-6h', '6-7h', '7-8h', '8-10h'])
        score_bins = pd.cut(df_filtered['Exam_Score'], bins=5, labels=['60-68', '68-76', '76-84', '84-92', '92-100'])
        
        heatmap_data = pd.crosstab(score_bins, sleep_bins)
        
        fig, ax = plt.subplots(figsize=(6, 5))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap=theme["heatmap"], ax=ax, cbar_kws={'label': 'Count'})
        ax.set_xlabel('Sleep Hours per Night')
        ax.set_ylabel('Exam Score Range')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    else:
        st.error('Required columns not found.')

# ROW 3:
col1_r3, col2_r3 = st.columns([1, 2])

with col1_r3:
    st.subheader("Outside Resources Proportions")
    st.write("The vast majority of students have access to the internet, regardless of their circumstances at home. Most students also have access to sufficient academic resources at home, and the same can be said for the help they receive in the form of parental involvement. All of these are crucial underlying factors that contribute to students' exam scores.")

with col2_r3:
    def pie_from_series(series, categories, title=""):
        s = pd.Categorical(series, categories=categories, ordered=True)
        counts = pd.Series(s).value_counts(dropna=True, sort=False)
        pie_df = counts.rename_axis("label").reset_index(name="count")

        if pie_df["count"].sum() == 0:  # CHANGED: guard for empty selection after filtering
            st.warning(f"No data to plot for {title}.")
            return

        fig = px.pie(
            pie_df,
            names="label",
            values="count",
            title=title,
            category_orders={"label": categories},
            hole=0.3,
            color="label",
            color_discrete_map=theme["pie_colors"],
        )
        fig.update_traces(textposition="inside", textinfo="percent+label", sort=False)
        fig.update_layout(
            title=dict(text=title, x=0.5, xanchor="center", y=1),
            showlegend=True,
            legend=dict(orientation="v", x=0.5, xanchor="center", y=-.1, yanchor="top"),
            height=360,
            margin=dict(l=10, r=10, t=40, b=80),
            uniformtext_minsize=10,
            uniformtext_mode="hide",
        )
        st.plotly_chart(fig, use_container_width=True)

    pie_col1, pie_col2, pie_col3 = st.columns(3)

    with pie_col1:
        pie_from_series(
            series=df_filtered["Internet_Access"],
            categories=["No", "Yes"],
            title="Internet Access"
        )

    with pie_col2:
        pie_from_series(
            series=df_filtered["Parental_Involvement"],
            categories=["Low", "Medium", "High"],
            title="Parental Involvement"
        )

    with pie_col3:
        pie_from_series(
            series=df_filtered["Access_to_Resources"],
            categories=["Low", "Medium", "High"],
            title="Access to Resources"
        )

st.divider()

# Footer
st.caption("**Data source:** https://www.kaggle.com/datasets/lainguyn123/student-performance-factors")

with st.expander("Data Preview"):
    st.dataframe(df)

# Read the CSV file for download
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Raw Data (CSV)",
    data=csv_data,
    file_name="StudentPerformanceFactors.csv",
    mime="text/csv",
)
