import streamlit as st
import pandas as pd

st.title("Bike Sharing Dashboard")
st.write("by : Axelino Natanael Ndahawali")

data = pd.read_csv("main_data.csv")

col1, col2 = st.columns(2)

with col1:
    workingday = data.groupby(by="workingday")["cnt"].sum()
    st.bar_chart(x=workingday.index,y=workingday.values)
with col2:
    weathersit = data.groupby(by="weathersit")["cnt"].sum()
    st.bar_chart(x=weathersit.index,y=weathersit.values)
