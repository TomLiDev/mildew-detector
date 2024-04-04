import streamlit as st

from app_pages.multi_page import MultiPage

from app_pages.page1 import page1_create
from app_pages.page2 import page2_create

app = MultiPage(app_name="This is the app test test woop test")

app.app_page("Page 1", page1_create)
app.app_page("Page 2nd", page2_create)

app.run()