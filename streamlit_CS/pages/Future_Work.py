import streamlit as st

st.set_page_config(
    page_title="Future Work",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Future Work")

st.subheader("Concrete Next Steps")

st.markdown(
    """
Here are several concrete directions I would pursue next with this project:

- Add forecasting for daily and monthly sales using time series models to estimate future revenue and demand by coffee type.
- Experiment with part A and B layouts, such as swapping the main heatmap with a time-series view, to see which arrangement users find more intuitive for answering business questions.
- Perform an accessibility audit on color choices and font sizes to better support users with vision disabilities.
- Add user-facing export and annotation features, allowing users perform actions such as downloading filtered views and capture snapshots.
    """
)

st.subheader("Reflection: From Lab 4.3 Prototype to Final Build")

st.markdown(
    """
- The prototype that I had helped to create for lab 4.3 was much more simplistic and generalized for its purpose.
- The final product had many more details/features that were not present in the prototype.
- The sidebar was not at all considered for the prototype, which was monumentally important for the functionality of the final product.
    """
)
