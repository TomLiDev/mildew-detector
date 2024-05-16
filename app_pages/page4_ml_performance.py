import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page4_create():
    """
    Page4_create function defines text and layout and presentation of figures
    displayed on the ML performance page.
    """
    st.write("## ML Performance")

    st.info(
        f"The figures below shows how the original leaf images dataset "
        f"was split into train, validation and test groups to facilitate the"
        f" development of an ML system with sufficient predictive accuracy on"
        f" healthy and powdery mildew infected leaves."
    )

    version = 'v2'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/"
                                     f"labels_distribution.png")
    st.image(labels_distribution, caption=f"Labels Distribution on Train, "
                                          f"Validation and Test Sets")
    st.write("---")

    #This section displays the pie chart showing distribution of images across
    #train, test and validation data sets. Note image capions are written
    #across multiple lines to comply with pep8.

    labels_distribution = plt.imread(f"outputs/{version}/"
                                     f"mildew_labels_distribution_pie.png")
    st.image(labels_distribution, caption="Pie Chart of Mildew Image "
                                          "Distribution on Train, Validation "
                                          "and Test Sets")
    labels_distribution = plt.imread(f"outputs/{version}/"
                                     f"healthy_labels_distribution_pie.png")
    st.image(labels_distribution, caption="Pie Chart of Healthy Image "
                                          "Distribution on Train, Validation "
                                          "and Test Sets")
    st.write("---")

    st.info(
        f"The figure below shows how the ML system was gradually trained and "
        f"improved over time, this is shown by the increase in accuracy and "
        f"reduction of loss. "
        f"Loss, also known as error function, quantifies how well a single "
        f"prediction of the ML system compares to the actual target value, "
        f"a healthy or powdery mildew infected leaf."
    )


    st.write("## Model Evolution")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                 index=['Loss', 'Accuracy']))
    st.write("---")
    