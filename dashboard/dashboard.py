import streamlit as st
import pandas as pd

st.title("Bike Sharing Dashboard")
st.write("by : Axelino Natanael Ndahawali")

data = pd.read_csv("./dashboard/main_data.csv")

col1, col2 = st.columns(2)

with col1:
    workingday_data = data.groupby(by=["workingday"],as_index=False)[["cnt"]].sum()
    st.bar_chart(workingday_data,x="workingday",y=["cnt"])
with col2:
    weathersit_data = data.groupby(by=["weathersit"],as_index=False)[["cnt"]].sum()
    st.bar_chart(weathersit_data,x="weathersit",y=["cnt"])

col3, col4 = st.columns(2)

with col3:
    season_data = data.groupby(by=["season"],as_index=False)[["cnt"]].sum()
    st.bar_chart(season_data,x="season",y=["cnt"])
with col4:
    yr_data = data.groupby(by=["yr"],as_index=False)[["cnt"]].sum()
    st.bar_chart(yr_data,x="yr",y=["cnt"])
