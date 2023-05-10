import streamlit as st
import pandas as pd

# Import functions

st.set_page_config(
    page_title="Title",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Header
title_column, logo_column = st.columns([3, 2])

with title_column:
    st.markdown('''
    # Title 🛠
    ### Sub Title
    ''')
