import streamlit as st


def page1_create():
    """
    This function defines the specific text and options displayed on page 1,
    the project overview page.
    """

    st.write("## Project Summary")
    st.write(
        "This project was undertaken with the aim of providing data analysis "
        "and a machine learning system which was able to solve the following "
        "business requirements."
        )

    st.info(
        f"Business Requirements \n\n"

        f"1 - Farmy & Foods are interested in conducting a study to visually" 
        f"differentiate a healthy cherry leaf from one with powdery mildew.\n\n"
        f"2 - Farmy & Foods are interested in predicting if a cherry leaf is"
        f"healthy or contains powdery mildew."
    )

    st.write("Project Hypothesis and Validation")
    if st.checkbox("Show Project Hypotheses and Validation Criteria"):

        st.info(
            f"1 - There will be a significant visual difference between healthy"
            f" and powdery mildew infected leaves which facilitates"
            f"differentiation between the two. \n\n"
            f"2 - Powdery mildew infected leaves will display a lower amount of"
            f" green on their surfaces. \n\n"
            f"3 - Healthy leaves will exhibit a greater amount of green" 
        )

        st.info(
            f"## Validation \n"
            f"Validation on whether or not the hypotheses are correct will "
            f"be determined by whether or not a Machine Learning system can "
            f"accurately, to a theshold of 98%, predict whether a leaf is "
            f"healthy or infected with powdery mildew."
        )
    st.write("---")
