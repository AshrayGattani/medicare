import streamlit as st
from predict import show_prediction
from explore import explore_page


page = st.sidebar.selectbox("Explore Or Predict",("Predict","Explore"))
if page=="Predict":
    show_prediction()
else:
    explore_page()
