import streamlit as st
import seaborn as sns
import pandas as pd
from cleaning_data import merged_engagement_df, household_spend_trends, category_spend_trends, category_units_trends, category_growth_spend, latest_year_spend_sorted

# Demographics and Engagement Section
with st.expander(label="Demographics and Engagement"):
    # Household Size vs Spend
    st.write("### Impact of Household Size on Total Spend")
    boxplot_data = merged_engagement_df.groupby('HH_SIZE')['SPEND'].mean().reset_index()
    st.bar_chart(boxplot_data.set_index('HH_SIZE')['SPEND'])
    
    # Presence of Children vs Spend
    st.write("### Impact of Presence of Children on Total Spend")
    boxplot_data_children = merged_engagement_df.groupby('CHILDREN')['SPEND'].mean().reset_index()
    st.bar_chart(boxplot_data_children.set_index('CHILDREN')['SPEND'])

    # Store Location vs Spend
    st.write("### Impact of Location on Total Spend")
    boxplot_data_store = merged_engagement_df.groupby('STORE_R')['SPEND'].mean().reset_index()
    st.bar_chart(boxplot_data_store.set_index('STORE_R')['SPEND'])

# Engagement over Time Section
with st.expander(label="Engagement over Time"):
    # Household Spending Trends Over Time
    st.write("### Household Spending Trends Over Time")
    st.line_chart(household_spend_trends.set_index('YEAR')['SPEND'])
    
    # Spending Trends by Product Category (Department) Over Time
    st.write("### Spending Trends by Product Category (Department) Over Time")
    category_spend_trends_pivot = category_spend_trends.pivot_table(values='SPEND', index='YEAR', columns='DEPARTMENT')
    st.line_chart(category_spend_trends_pivot)

    # Units Sold by Product Category Over Time
    st.write("### Units Sold by Product Category Over Time")
    category_units_trends_pivot = category_units_trends.pivot_table(values='UNITS', index='YEAR', columns='DEPARTMENT')
    st.line_chart(category_units_trends_pivot)

    # Percentage Change in Spending by Department (Year-over-Year)
    st.write("### Percentage Change in Spending by Department (Year-over-Year)")
    st.write("This is a heatmap showing the percentage change in spending by department.")
    st.dataframe(category_growth_spend)

    # Top 10 Product Categories by Total Spend in 2019
    st.write("### Top 10 Product Categories by Total Spend in 2019")
    top_10_departments = latest_year_spend_sorted.head(10)
    st.bar_chart(top_10_departments.set_index('DEPARTMENT')['SPEND'])
    
    # Bottom 10 Product Categories by Total Spend in 2019
    st.write("### Bottom 10 Product Categories by Total Spend in 2019")
    bottom_10_departments = latest_year_spend_sorted.tail(10)
    st.bar_chart(bottom_10_departments.set_index('DEPARTMENT')['SPEND'])
