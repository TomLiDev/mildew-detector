"""
Overall controlling python code for the streamlit dashboard app
"""

import streamlit as st

from app_pages.multi_page import MultiPage

from app_pages.page1_overview import page1_create
from app_pages.page2_leaves_visualiser import page2_create
from app_pages.page3_mildew_detector import page3_create
from app_pages.page4_ml_performance import page4_create
from app_pages.page5_hypothesis import page5_create

"""
Code below will create an instance of the streamlit app
"""
app = MultiPage(app_name="Mildew Detector and Predictor")

app.app_page("Project Overview", page1_create)
app.app_page("Leaves Visualiser", page2_create)
app.app_page("Mildew Detector", page3_create)
app.app_page("ML Performance", page4_create)
app.app_page("Project Hypotheses", page5_create)

app.run()