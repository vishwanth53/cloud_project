import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from cleaning_data import merged_engagement_df, household_spend_trends, category_spend_trends, category_units_trends, category_growth_spend, latest_year_spend_sorted

# Custom Colors for Bar Charts and Line Charts
bar_colors = ['#FF6347', '#4682B4', '#32CD32']  # Example colors for bar charts (Tomato, SteelBlue, LimeGreen)
line_colors = ['#FF4500', '#1E90FF', '#32CD32']  # Example colors for line charts (OrangeRed, DodgerBlue, LimeGreen)

# Demographics and Engagement Section
with st.expander(label="Demographics and Engagement"):
    # Household Size vs Spend
    st.write("### Impact of Household Size on Total Spend")
    boxplot_data = merged_engagement_df.groupby('HH_SIZE')['SPEND'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(boxplot_data['HH_SIZE'], boxplot_data['SPEND'], color=bar_colors[0])  # Set bar color
    ax.set_title("Impact of Household Size on Total Spend")
    ax.set_xlabel("Household Size")
    ax.set_ylabel("Average Spend")
    st.pyplot(fig)

    # Presence of Children vs Spend
    st.write("### Impact of Presence of Children on Total Spend")
    boxplot_data_children = merged_engagement_df.groupby('CHILDREN')['SPEND'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(boxplot_data_children['CHILDREN'], boxplot_data_children['SPEND'], color=bar_colors[1])  # Set bar color
    ax.set_title("Impact of Presence of Children on Total Spend")
    ax.set_xlabel("Presence of Children")
    ax.set_ylabel("Average Spend")
    st.pyplot(fig)

    # Store Location vs Spend
    st.write("### Impact of Location on Total Spend")
    boxplot_data_store = merged_engagement_df.groupby('STORE_R')['SPEND'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(boxplot_data_store['STORE_R'], boxplot_data_store['SPEND'], color=bar_colors[2])  # Set bar color
    ax.set_title("Impact of Location on Total Spend")
    ax.set_xlabel("Store Location")
    ax.set_ylabel("Average Spend")
    st.pyplot(fig)

# Engagement over Time Section
with st.expander(label="Engagement over Time"):
    # Household Spending Trends Over Time
    st.write("### Household Spending Trends Over Time")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(household_spend_trends['YEAR'], household_spend_trends['SPEND'], color=line_colors[0], lw=2)  # Set line color
    ax.set_title("Household Spending Trends Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Spend")
    st.pyplot(fig)

    # Spending Trends by Product Category (Department) Over Time
    st.write("### Spending Trends by Product Category (Department) Over Time")
    category_spend_trends_pivot = category_spend_trends.pivot_table(values='SPEND', index='YEAR', columns='DEPARTMENT')
    fig, ax = plt.subplots(figsize=(10, 6))
    for department in category_spend_trends_pivot.columns:
        ax.plot(category_spend_trends_pivot.index, category_spend_trends_pivot[department], label=department, lw=2)
    ax.set_title("Spending Trends by Product Category Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Spend")
    ax.legend(title="Product Category")
    st.pyplot(fig)

    # Units Sold by Product Category Over Time
    st.write("### Units Sold by Product Category Over Time")
    category_units_trends_pivot = category_units_trends.pivot_table(values='UNITS', index='YEAR', columns='DEPARTMENT')
    fig, ax = plt.subplots(figsize=(10, 6))
    for department in category_units_trends_pivot.columns:
        ax.plot(category_units_trends_pivot.index, category_units_trends_pivot[department], label=department, lw=2)
    ax.set_title("Units Sold by Product Category Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Units Sold")
    ax.legend(title="Product Category")
    st.pyplot(fig)

    # Percentage Change in Spending by Department (Year-over-Year)
    st.write("### Percentage Change in Spending by Department (Year-over-Year)")
    st.write("This is a heatmap showing the percentage change in spending by department.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(category_growth_spend, annot=True, cmap="coolwarm", ax=ax)  # Adjust colormap as needed
    ax.set_title("Percentage Change in Spending by Department (Year-over-Year)")
    st.pyplot(fig)

    # Top 10 Product Categories by Total Spend in 2019
    st.write("### Top 10 Product Categories by Total Spend in 2019")
    top_10_departments = latest_year_spend_sorted.head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(top_10_departments['DEPARTMENT'], top_10_departments['SPEND'], color=bar_colors[0])  # Set bar color
    ax.set_title("Top 10 Product Categories by Total Spend in 2019")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Spend")
    ax.set_xticklabels(top_10_departments['DEPARTMENT'], rotation=45, ha="right")
    st.pyplot(fig)

    # Bottom 10 Product Categories by Total Spend in 2019
    st.write("### Bottom 10 Product Categories by Total Spend in 2019")
    bottom_10_departments = latest_year_spend_sorted.tail(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(bottom_10_departments['DEPARTMENT'], bottom_10_departments['SPEND'], color=bar_colors[1])  # Set bar color
    ax.set_title("Bottom 10 Product Categories by Total Spend in 2019")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Spend")
    ax.set_xticklabels(bottom_10_departments['DEPARTMENT'], rotation=45, ha="right")
    st.pyplot(fig)


