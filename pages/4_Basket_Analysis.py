import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from cleaning_data import encoded_df, final_df


# Generate frequent itemsets and association rules
frequent_itemsets = apriori(encoded_df, min_support=0.001, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.3)

# Streamlit UI
st.title("Association Rules for Retail Basket Analysis")

# Displaying the association rules if they exist
if not rules.empty:
    st.subheader("Association Rules")
    
    # Display the rules table
    st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())
    
    # Provide a summary
    st.write(f"Number of rules generated: {len(rules)}")
    
    # Allow user to filter by support or confidence if desired
    min_support = st.slider("Minimum Support", 0.001, 0.1, 0.01, 0.001)
    min_confidence = st.slider("Minimum Confidence", 0.1, 1.0, 0.5, 0.01)
    
    # Filter rules based on user input
    filtered_rules = rules[(rules['support'] >= min_support) & (rules['confidence'] >= min_confidence)]
    
    # Display filtered rules
    st.subheader("Filtered Association Rules")
    st.dataframe(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
else:
    st.write("No association rules generated with the current thresholds.")
