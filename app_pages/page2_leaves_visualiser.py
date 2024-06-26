import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page2_create():
    """
    Page2_create function below defines text shown on the leaf visulisation 
    page and retrieves figures from the relevant version folder if boxes are
    checked.
    """

    st.write("## Leaves Visualiser")

    version = 'v2'

    if st.checkbox(
        f"Show average and variability images for healthy leaves"
        f" and those infected with Powdery Mildew."
        ):

        st.info(
            f"Showing images from {version}"
        )

        avg_powdery_mildew = plt.imread(f"outputs/{version}/"
        f"avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(avg_powdery_mildew, caption=f"Average and Variability Image "
        f"of Leaf infected with Powdery Mildew")
        st.image(avg_healthy, caption=f"Average and Variability Image of "
                                      f"healthy leaf")

    
    if st.checkbox(f"Show figures for differences between average health and "
                   f"Powdery Mildew leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.image(diff_between_avgs, caption=f"Difference between average "
                                            f"images")
    
    st.info(
            f"As shown in the figures above, leaves infected with powdery "
            f"mildew generally show a greater amount of white pixels in the "
            f"images "
            f"with the healthy leaves showing a much more solid, overall "
            f"green colouring. This is in support of the project hypotheses."
        )

    if st.checkbox("Image Montage"): 
        st.write(f"* To refresh the montage, click on the 'Create Montage' "
                 f"button")
        my_data_dir = 'inputs/mildew_dataset/cherry-leaves/resized'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels,
                                        index=0)
        if st.button("Create Montage"):      
            image_montage(dir_path= my_data_dir + '/validation',
                        label_to_display=label_to_display,
                        nrows=8, ncols=3, figsize=(10,25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    """
    This is the function for creating the image montage specifically.
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class to display
    if label_to_display in labels:

        # checks if montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/'+ label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return
        

        # create list of axes indices based on nrows and ncols
        list_rows= range(0,nrows)
        list_cols= range(0,ncols)
        plot_idx = list(itertools.product(list_rows,list_cols))


        #This creates the figure and displays the images
        fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
        for x in range(0,nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width "
            f"{img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()
        
        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
    st.write("---")
