import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Professional Bio",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Biography")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Profile")

    # Optional local profile image
    # Put an image at:  <project_root>/images/profile.jpg
    image_path = Path(__file__).parent.parent / "images" / "profile.jpg"

    if image_path.exists():
        st.image(
            image_path,
            caption="Photo of Kevin Kruzel",
            use_column_width=True,
        )
    else:
        st.info(
            "Add a profile image at `images/profile.jpg` to display it here."
        )

with col2:
    st.subheader("Professional Summary")

    st.markdown(
        """
I’m an undergraduate Mathematics student at MSU Denver with a strong focus on data science,
statistics, and analytics. Most of my work combines Python, R, and SQL with tools like Pandas,
Plotly, and Streamlit to explore real-world datasets and communicate insights clearly.
I’m especially interested in machine learning, data visualization, and statistics. I
enjoy building small analytical products that feel like real tools, not just class assignments.
My long-term goal is to work in a role where I can turn messy data into clear, ethical,
and visually appealing stories for everyone to see.
        """
    )

st.subheader("Highlights")

st.markdown(
    """
- Coursework in Mathematics, Data Science, and Statistics at MSU Denver.
- Experience with Python, R , and SQL.
- Comfortable building interactive dashboards and apps in Streamlit with Plotly.
- Hands-on projects in data visualization and machine learning.
    """
)

st.subheader("Visualization Philosophy")

st.markdown(
    """
My visualization philosophy centers on **clarity**, **accessibility**, and **ethics**:

- **Clarity:** Every chart should answer a specific question and avoid unnecessary decoration.
- **Accessibility:** I aim for readable color choices, clear labels, and designs that reflect the ideas of the project.
- **Ethics:** I try to present data honestly by avoiding false conclusions and avoid over-claiming what the data can say.
    """
)
