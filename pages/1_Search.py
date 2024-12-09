import streamlit as st
from cleaning_data import final_df

# Sidebar for filtering and sorting options
st.sidebar.header("Filter and Sort Options")

# 1. Filter by HSHD_NUM
hshd_num_search = st.sidebar.text_input("Filter by HSHD_NUM:", placeholder="Enter HSHD_NUM")

if hshd_num_search:
    filtered_df = final_df[final_df['HSHD_NUM'].astype(str).str.contains(hshd_num_search)]
else:
    filtered_df = final_df

# 2. Sort options
sort_by = st.sidebar.selectbox(
    "Sort by column:",
    options=["HSHD_NUM", "BASKET_NUM", "PURCHASE_", "PRODUCT_NUM", "DEPARTMENT", "COMMODITY"]
)
sort_order = st.sidebar.checkbox("Sort descending?", value=False)

# Sorting the DataFrame based on user input
sorted_df = filtered_df.sort_values(by=sort_by, ascending=not sort_order)

# Main content area
st.header("Filtered and Sorted Data")
st.write(f"Displaying data sorted by `{sort_by}` in {'descending' if sort_order else 'ascending'} order.")
st.dataframe(sorted_df)

# Add additional information or statistics about the filtered dataset
st.subheader("Summary Statistics")
st.write(sorted_df.describe())
