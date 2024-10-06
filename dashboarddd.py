import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

air_quality_df = ('https://raw.githubusercontent.com/fahmii1112/Proyek-analisis-data/refs/heads/main/air_quality.csv')

st.header('Proyek analisis :sparkles:')

st.subheader('kualitas udara')
 
 
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    air_quality_df["RAIN"],
    air_quality_df["SO2"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)
