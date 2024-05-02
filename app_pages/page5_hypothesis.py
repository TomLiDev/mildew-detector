import streamlit as st
import matplotlib.pyplot as plt

version = 'v2'

def page5_create():
    """
    Page5_create function defines text and layout of information displayed
    on the project hypotheses and validation page.
    """
    st.write("## Business Value Delivered")

    st.info(
        f"The confirmation of the project hypotheses as detailed "
        f"below demonstrates the success and accuracy of this ML system "
        f"to predict and identify leaves with powdery mildew vs those that "
        f" are healthy. \n\n"
        f"This delivers value to Farmy & Foods in drastically reducing the "
        f"time and resource required to identify cherry plants infected "
        f"with powdery mildew. This makes quality control much more efficient"
        f" and ensures that fruit of poor quality is not "
        f"provided to consumers, keeping standards high, protecting the "
        f"businesses reputation and ensuring ongoing revenue."
    )
    st.write("---")

    st.write("## Project Hypotheses and Validation")
    if st.checkbox('Show Green Pixel Analysis'):
        st.info(
            f"As shown in the figures below, the healthy leaf images show "
            f"a significantly higher number of green pixels than those "
            f"images where the leaf is infected with powdery mildew. This "
            f"is clear support for the project hypotheses.  \n\n"
            f"The asterisk on the Number of Pixels Y axis, is because the "
            f"value is not exactly the number of green pixels per image, but "
            f"a simplified, representative value which is displayed more "
            f"easily on the figure axis."
        )
        healthy = plt.imread(f"outputs/{version}/healthy_pixels.png")
        mildew = plt.imread(f"outputs/{version}/powdery_mildew_pixels.png")

        st.image(healthy)
        st.image(mildew)

    st.write("### Hypothesis 1:")
    st.write(
        f"There will be a significant visual difference between healthy "
        f"and powdery mildew infected leaves which facilitates "
        f"differentiation between the two. \n\n"
        f"Was this Hypothesis correct?"
    )

    st.success(
        f"Yes. \n\n"
        f"A clear visual difference between healthy and powdery mildew "
        f"leaves facilitates an ML model which is able to accurately predict "
        f"the difference with greater than 97% accuracy."
    )

    st.write("### Hypothesis 2:")
    st.write(
        f"2 - Powdery mildew infected leaves will display a lower amount of"
        f" green on their surfaces. \n\n"
        f"Was this Hypothesis correct?"
    )

    st.success(
        f"Yes. \n\n"
        f"The presence of less green, clearly visible in images"
        f" of leaves with powdery mildew, differentiates them from healthy."
    )

    st.write("### Hypothesis 3:")
    st.write(
        f"Healthy leaves will exhibit a greater amount of green \n\n"
        f"Was this Hypothesis correct?" 
    )

    st.success(
        f"Yes. \n\n"
        f"The greater number of green pixels in images of healthy leaves "
        f"clearly differentiates them from those infected with powdery mildew."
    )
    st.write("---")