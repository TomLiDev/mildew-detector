import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results, np.float32 types need to converted
    to float64 otherwise the function returns a value error
    """
    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Infected': 0, 'Uninfected': 1}.keys(),
        columns=['Probability']
    )
    new = np.float64(pred_proba)
    prob_per_class.loc[pred_class] = new

    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    # below lines customise colour used in chart
    if pred_class == 'Infected':
        colour = 'red'
    else:
        colour = 'green'

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300,
        title=f"Prediction Probability on {pred_class} Leaf Identification")
    fig.update_traces(marker_color=colour)
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    version = 'v2'
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]))

    img_to_use = img_resized.convert('RGB')
    my_image = np.expand_dims(img_to_use, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/mildew_detector_model.h5")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Uninfected': 0, 'Infected': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
       pred_proba = 1 - pred_proba

    if pred_class == 'Infected':
        st.error(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}** with powdery mildew.")
    else:
        st.success(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}** with powdery mildew.")

    

    return pred_proba, pred_class