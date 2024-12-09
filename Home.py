import streamlit as st
from cleaning_data import final_df
import pandas as pd

# Ensure 'PURCHASE_' column is in datetime format
final_df['PURCHASE_'] = pd.to_datetime(final_df['PURCHASE_'], errors='coerce')

with st.sidebar:
    st.header('Machine Learning Assignment')

st.dataframe(final_df)

# Options for sorting
options = ["HSHD_NUM", "BASKET_NUM", "DATE", "PRODUCT_NUM", "DEPARTMENT", "COMMODITY", "PURCHASE_"]

# Use a radio button instead of a selectbox
selection = st.radio(label="Sort by:", options=options)

# Display the sorted dataframe based on the selected column
if selection == "HSHD_NUM":
    st.dataframe(final_df.sort_values(by='HSHD_NUM', ascending=False))
elif selection == "BASKET_NUM":
    st.dataframe(final_df.sort_values(by='BASKET_NUM', ascending=False))
elif selection == "DATE":
    st.dataframe(final_df.sort_values(by='PURCHASE_', ascending=False))
elif selection == "PRODUCT_NUM":
    st.dataframe(final_df.sort_values(by='PRODUCT_NUM', ascending=False))
elif selection == "DEPARTMENT":
    st.dataframe(final_df.sort_values(by='DEPARTMENT', ascending=False))
elif selection == "PURCHASE_":
    st.info("Latest Transaction Details.")
    st.dataframe(final_df.sort_values(by='PURCHASE_', ascending=False))
else:
    st.dataframe(final_df.sort_values(by='COMMODITY', ascending=False))
