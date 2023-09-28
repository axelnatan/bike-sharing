import streamlit as st
import pandas as pd

st.title("Bike Sharing Dashboard")
st.write("by : Axelino Natanael Ndahawali")

data = pd.read_csv("./dashboard/main_data.csv")

col1, col2 = st.columns(2)

with col1:
    workingday_data = data.groupby(by=["workingday","day"],as_index=False)["cnt"].sum()
    st.bar_chart(workingday_data,x="day",y=["cnt"])
with col2:
    weathersit_data = data.groupby(by=["weathersit","weather"],as_index=False)["cnt"].sum()
    st.bar_chart(weathersit_data,x="weather",y=["cnt"])
