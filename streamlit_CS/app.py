import streamlit as st

st.set_page_config(
    page_title="Coffee Sales - Project 2",
    page_icon="☕",
    layout="wide"
)

st.title("Coffee Sales - Project 2 by Kevin Kruzel")

st.markdown(
    """
    ### ☕ About this Project
    
    This project explores and analyzes the factors that influence the revenue a coffee shop earns using a dataset
    containing the details 3,547 transactions taken over the time period of about a year. This website uses several
    pages to explore the entire process behind the analysis.
    
    **Pages:**
    - ☕ **app** - Overview of the Project
    - 📄 **Bio** - Professional bio of Kevin Kruzel
    - 📊 **EDA Gallery** - Exploratory data analysis of the dataset, complete with charts and initial observations
    - 📈 **Dashboard** - Visuals that help explore the dataset in more depth
    - 🧭 **Future Works** - Next steps and reflection of the project
    
    Navigate using the sidebar to begin exploring the other pages of the project.
    """
)

st.caption("Built with Streamlit • Class template")
