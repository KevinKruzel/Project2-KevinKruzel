import streamlit as st

st.set_page_config(
    page_title="Student Performance Factors",
    page_icon="📊",
    layout="wide"
)

st.title("Student Performance Factors")

st.markdown(
    """
    ### 📚 About This Dashboard
    
    This interactive dashboard analyzes factors that influence student academic performance based on a dataset 
    of over 6,000 students. Explore how various elements correlate with exam scores.
    
    **Key Features:**
    - 🎨 **Customizable Themes** - Choose from 6 color schemes
    - 📊 **Interactive Filters** - Filter by gender, income, school type, and attendance
    - 📈 **Visual Analytics** - Scatter plots, heatmaps, and pie charts
    - 💾 **Data Export** - Download the raw dataset for further analysis
    
    **Navigate to the Student Factors page** using the sidebar to begin exploring the data.
    """
)

with st.expander("How this app is organized (for students)"):
    st.write(
        """
        - `app.py` is the entry point.
        - Pages live in the `/pages` folder and auto-appear in the sidebar.
        """
    )

st.caption("Built with Streamlit • Class template")
