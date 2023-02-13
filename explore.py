import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt





@st.cache
def load_data():
    df = pd.read_csv("HackathonData.csv")
    return df

df = load_data()

def explore_page():
    return 
  