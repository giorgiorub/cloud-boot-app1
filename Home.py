import pandas as pd
import streamlit as st

st.title("Hello everyone!")

st.header("This is a Streamlit header!")

df = pd.read_csv("https://storage.googleapis.com/cloud-boot-app-bucket/1553768847-housing.csv")

st.dataframe(df)
