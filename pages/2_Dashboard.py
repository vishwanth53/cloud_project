import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from cleaning_data import (
    seasonal_sales,
    seasonal_footfall,
    top_products_per_season,
    inventory_recommendation,
    brand_preference,
    organic_preference
)

# Setting up Tabs
tab1, tab2 = st.tabs(["Seasonal Trends", "Brand and Organic Preferences"])

# Tab 1: Seasonal Trends
with tab1:
    st.subheader("Seasonal Trends")
    st.markdown("Explore how sales, customer footfall, and top products vary by season.")

    # Plot 1: Total Sales by Season
    st.write("#### Total Sales by Season")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=seasonal_sales, x='season', y='SPEND', ax=ax1)
    ax1.set_title('Total Sales by Season')
    ax1.set_xlabel('Season')
    ax1.set_ylabel('Total Sales')
    st.pyplot(fig1)

    # Plot 2: Customer Footfall by Season
    st.write("#### Customer Footfall by Season")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=seasonal_footfall, x='season', y='BASKET_NUM', ax=ax2)
    ax2.set_title('Customer Footfall by Season')
    ax2.set_xlabel('Season')
    ax2.set_ylabel('Customer Footfall')
    st.pyplot(fig2)

    # Plot 3: Top Products by Season
    st.write("#### Top 5 Products by Season")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_products_per_season, x='PRODUCT_NUM', y='SPEND', hue='season', ax=ax3)
    ax3.set_title('Top 5 Products by Season')
    ax3.set_xlabel('Product Number')
    ax3.set_ylabel('Total Sales')
    st.pyplot(fig3)

    # Inventory Recommendation
    st.write("#### Inventory Recommendations")
    st.text(inventory_recommendation)

# Tab 2: Brand and Organic Preferences
with tab2:
    st.subheader("Brand and Organic Preferences")
    st.markdown("Analyze customer preferences for private vs national brands and organic vs non-organic products.")

    # Plot 4: Total Spend for Private vs National Brands
    st.write("#### Total Spend for Private vs National Brands")
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    brand_preference['SPEND'].plot(kind='bar', color=['#4CAF50', '#2196F3'], ax=ax4)
    ax4.set_title('Total Spend for Private vs National Brands')
    ax4.set_ylabel('Total Spend')
    ax4.set_xticks(range(len(brand_preference)))
    ax4.set_xticklabels(brand_preference.index, rotation=0)
    st.pyplot(fig4)

    # Plot 5: Total Units Sold for Private vs National Brands
    st.write("#### Total Units Sold for Private vs National Brands")
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    brand_preference['UNITS'].plot(kind='bar', color=['#4CAF50', '#2196F3'], ax=ax5)
    ax5.set_title('Total Units Sold for Private vs National Brands')
    ax5.set_ylabel('Total Units Sold')
    ax5.set_xticks(range(len(brand_preference)))
    ax5.set_xticklabels(brand_preference.index, rotation=0)
    st.pyplot(fig5)

    # Plot 6: Total Spend for Organic vs Non-Organic Products
    st.write("#### Total Spend for Organic vs Non-Organic Products")
    fig6, ax6 = plt.subplots(figsize=(10, 6))
    organic_preference['SPEND'].plot(kind='bar', color=['#FF5722', '#9E9E9E'], ax=ax6)
    ax6.set_title('Total Spend for Organic vs Non-Organic Products')
    ax6.set_ylabel('Total Spend')
    ax6.set_xticks(range(len(organic_preference)))
    ax6.set_xticklabels(organic_preference.index, rotation=0)
    st.pyplot(fig6)

    # Plot 7: Total Units Sold for Organic vs Non-Organic Products
    st.write("#### Total Units Sold for Organic vs Non-Organic Products")
    fig7, ax7 = plt.subplots(figsize=(10, 6))
    organic_preference['UNITS'].plot(kind='bar', color=['#FF5722', '#9E9E9E'], ax=ax7)
    ax7.set_title('Total Units Sold for Organic vs Non-Organic Products')
    ax7.set_ylabel('Total Units Sold')
    ax7.set_xticks(range(len(organic_preference)))
    ax7.set_xticklabels(organic_preference.index, rotation=0)
    st.pyplot(fig7)

