import streamlit as st

def page1_create():
    st.write("Project Summary")
    st.write(
        "This project was undertaken with the aim of providing data analysis"
        "and a machine learning system which was able to solve the following "
        "business requirements."
        )

    st.info(
        f"Business Requirements \n\n"

        f"1 - The client is interested in conducting a study to visually" 
        f"differentiate a healthy cherry leaf from one with powdery mildew.\n\n"
        f"2 - The client is interested in predicting if a cherry leaf is"
        f"healthy or contains powdery mildew."
    )

    st.write("Project Hypothesis and Validation")
    st.write(
        f"Null Hypothesis - There will be no significant visual difference "
        f"between powdery mildew-infected and healthy cherry leaves."
    )
    st.write(
        f"Alternative Hypothesis - There will be a significant visual "
        f"difference between powdery mildew-infected and healthy cherry leaves" 
        f"facilitating visual identification and prediction of whether or not"
        f"a cherry leaf is infected with powdery mildew."
    )
    st.write(
        f"Validation - A machine learning system will be used to accept or "
        f"reject the project hypotheses. If, after sufficient relevant"
        f"training and fitting to leaf image data, a machine learning system"
        f"cannot accurately visually differentiate between a healthy cherry"
        f"leaf and one infected with powdery mildew then the alternative"
        f"hypothesis will be rejected and the null hypothesis accepted. If a"
        f"machine learning system can predict whether or not a leaf is healthy"
        f"or infected with powdery mildew with an accuracy greater than 98%"
        f"the null hypothesis will be rejected and the alternative hypothesis"
        f"will be accepted."
    )
