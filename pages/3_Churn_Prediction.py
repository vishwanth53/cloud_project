import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from cleaning_data import correlation_matrix, customer_engagement

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["Correlation Analysis", "Total Spend Trends", "Purchase Frequency Trends"])

# Tab 1: Correlation Analysis
with tab1:
    st.subheader("Correlation Analysis Between Disengagement and Demographics")
    st.markdown(
        """
        This heatmap showcases the correlation between various demographic features and disengagement.
        Darker shades indicate stronger positive or negative correlations.
        """
    )
    # Displaying heatmap using matplotlib and Streamlit
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Analysis Between Disengagement and Demographics", fontsize=14)
    st.pyplot(fig)

# Tab 2: Total Spend Trends
with tab2:
    st.subheader("Total Spend Trends by Disengagement Status")
    st.markdown(
        """
        Analyze the total spending trends over the years based on customer disengagement status.
        Use this chart to identify how disengaged customers' spending patterns differ from engaged customers.
        """
    )
    # Grouping and plotting the data
    total_spend_trends = customer_engagement.groupby(['year', 'disengaged'])['total_spend'].sum().unstack()
    st.line_chart(total_spend_trends)

# Tab 3: Purchase Frequency Trends
with tab3:
    st.subheader("Purchase Frequency Trends by Disengagement Status")
    st.markdown(
        """
        This chart highlights how frequently purchases are made by engaged and disengaged customers over the years.
        Use it to observe shifts in engagement levels and their impact on purchase frequency.
        """
    )
    # Grouping and plotting the data
    purchase_frequency_trends = customer_engagement.groupby(['year', 'disengaged'])['frequency_of_purchase'].sum().unstack()
    st.line_chart(purchase_frequency_trends)
