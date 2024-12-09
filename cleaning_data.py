import pandas as pd
import numpy as np

households_df = pd.read_csv('./datasets/households.csv')
products_df = pd.read_csv('./datasets/products.csv')
transactions_df = pd.read_csv('./datasets/transactions.csv')

households_df.isnull().sum().sum()

households_df.replace(r'^\s*null\s*$', np.nan, regex=True, inplace=True)

for column in households_df.columns:
    if households_df[column].dtype == 'object':
        households_df[column].fillna(households_df[column].mode()[0], inplace=True)
        
households_df.isnull().sum()
products_df.isnull().sum()
transactions_df.isnull().sum()

households_df.columns = households_df.columns.str.replace(r'\s+', '', regex=True)
products_df.columns = products_df.columns.str.replace(r'\s+', '', regex=True)
transactions_df.columns = transactions_df.columns.str.replace(r'\s+', '', regex=True)

households_transactions = pd.merge(
    transactions_df,
    households_df,
    how='inner',
    on='HSHD_NUM'
)

final_df = pd.merge(
    households_transactions,
    products_df,
    how='inner',
    on='PRODUCT_NUM'
)

final_df['SPEND'] = pd.to_numeric(final_df['SPEND'], errors='coerce')
final_df['UNITS'] = pd.to_numeric(final_df['UNITS'], errors='coerce')

# Fill missing values in 'SPEND' and 'UNITS' with 0 (assuming missing values mean no purchase)
final_df['SPEND'].fillna(0, inplace=True)
final_df['UNITS'].fillna(0, inplace=True)

# 2. Feature Engineering: Calculate customer engagement metrics
# For example, customer engagement can be measured by total spend, total units bought, and number of transactions

engagement_df = final_df.groupby('HSHD_NUM').agg({
    'SPEND': 'sum',    # Total spend per household
    'UNITS': 'sum',    # Total units bought per household
    'BASKET_NUM': 'nunique'  # Number of unique transactions per household
}).reset_index()

# 3. Merge customer engagement metrics with household factors
merged_engagement_df = pd.merge(engagement_df, final_df[['HSHD_NUM', 'HH_SIZE', 'CHILDREN', 'STORE_R', 'INCOME_RANGE']], on='HSHD_NUM', how='left')

merged_engagement_df['CHILDREN'] = merged_engagement_df['CHILDREN'].replace({'Y': 1, 'N': 0})

from scipy import stats

household_size_groups = [group['SPEND'].values for name, group in merged_engagement_df.groupby('HH_SIZE')]
f_stat, p_val = stats.f_oneway(*household_size_groups)
#print(f"ANOVA - Household Size vs Total Spend: F-stat = {f_stat}, p-value = {p_val}")

children_groups = [group['SPEND'].values for name, group in merged_engagement_df.groupby('CHILDREN')]
f_stat, p_val = stats.f_oneway(*children_groups)
#print(f"ANOVA - Presence of Children vs Total Spend: F-stat = {f_stat}, p-value = {p_val}")

household_spend_trends = final_df.groupby('YEAR')['SPEND'].sum().reset_index()

category_spend_trends = final_df.groupby(['YEAR', 'DEPARTMENT'])['SPEND'].sum().reset_index()

category_units_trends = final_df.groupby(['YEAR', 'DEPARTMENT'])['UNITS'].sum().reset_index()

category_growth_spend = category_spend_trends.pivot(index='YEAR', columns='DEPARTMENT', values='SPEND')
category_growth_spend = category_growth_spend.pct_change(axis='index') * 100

latest_year_spend = final_df[final_df['YEAR'] == 2019].groupby('DEPARTMENT')['SPEND'].sum().reset_index()

latest_year_spend_sorted = latest_year_spend.sort_values(by='SPEND', ascending=False)

final_df['PURCHASE_DATE'] = pd.to_datetime(final_df['PURCHASE_'], format='%d-%b-%y')
final_df['year'] = final_df['PURCHASE_DATE'].dt.year

# Aggregate total spend, frequency of purchase, and recency
customer_engagement = final_df.groupby(['HSHD_NUM', 'year']).agg(
    total_spend=('SPEND', 'sum'),
    frequency_of_purchase=('BASKET_NUM', 'nunique'),
    recency_of_purchase=('PURCHASE_DATE', lambda x: (x.max() - x.min()).days)
).reset_index()

# Step 2: Identify Disengaged Customers
# Calculate the difference in spending and frequency between consecutive years
customer_engagement['spend_diff'] = customer_engagement.groupby('HSHD_NUM')['total_spend'].diff()
customer_engagement['frequency_diff'] = customer_engagement.groupby('HSHD_NUM')['frequency_of_purchase'].diff()

# Define disengagement criteria: If the spend or frequency drops significantly between 2018 and 2019
customer_engagement['disengaged'] = np.where((customer_engagement['spend_diff'] < -0.2) | 
                                             (customer_engagement['frequency_diff'] < -0.2), 1, 0)


demographics = final_df[['HSHD_NUM', 'AGE_RANGE', 'INCOME_RANGE']].drop_duplicates()

# Merge demographics with engagement data
customer_engagement = customer_engagement.merge(demographics, on='HSHD_NUM', how='left')

# Correlation between disengagement and demographics
correlation = customer_engagement[['disengaged', 'AGE_RANGE', 'INCOME_RANGE']].copy()

# Map categorical variables to numerical values for correlation
correlation['AGE_RANGE'] = correlation['AGE_RANGE'].astype('category').cat.codes
correlation['INCOME_RANGE'] = correlation['INCOME_RANGE'].astype('category').cat.codes

correlation_matrix = correlation.corr()

# Group transactions by BASKET_NUM and aggregate the products
transaction_data = final_df.groupby('BASKET_NUM')['PRODUCT_NUM'].apply(list)

# Convert to DataFrame
transaction_df = pd.DataFrame({'BASKET_NUM': transaction_data.index, 'PRODUCTS': transaction_data.values})

# Display sample transactions
#print(transaction_df.head())

from mlxtend.preprocessing import TransactionEncoder

# Initialize TransactionEncoder
te = TransactionEncoder()

# Transform the transactions into one-hot encoded format
te_data = te.fit(transaction_df['PRODUCTS']).transform(transaction_df['PRODUCTS'])

# Convert to DataFrame
encoded_df = pd.DataFrame(te_data, columns=te.columns_)

# Display the encoded data
#print(encoded_df.head())

from mlxtend.frequent_patterns import apriori, association_rules

# Apply Apriori to find frequent itemsets
frequent_itemsets = apriori(encoded_df, min_support=0.0005, use_colnames=True)

# Display frequent itemsets
#print(frequent_itemsets.head())

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.05)

# Display association rules
#print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())

final_df['PURCHASE_DATE'] = pd.to_datetime(final_df['PURCHASE_'], format='%d-%b-%y')

# Assign season based on month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

final_df['season'] = final_df['PURCHASE_DATE'].dt.month.apply(get_season)

seasonal_sales = final_df.groupby(['season'])['SPEND'].sum().reset_index()
seasonal_footfall = final_df.groupby(['season'])['BASKET_NUM'].nunique().reset_index()

seasonal_product_sales = final_df.groupby(['season', 'PRODUCT_NUM'])['SPEND'].sum().reset_index()

# Identify top products by season (for example, top 5 products in each season)
top_products_per_season = seasonal_product_sales.groupby('season').apply(lambda x: x.nlargest(5, 'SPEND')).reset_index(drop=True)

high_demand_products = top_products_per_season[['season', 'PRODUCT_NUM']]

# Assuming a recommendation logic to suggest inventory for products with seasonal spikes
inventory_recommendation = high_demand_products.groupby('season')['PRODUCT_NUM'].apply(list).reset_index()

#BRand preferences:
brand_preference = final_df.groupby('BRAND_TY')[['SPEND', 'UNITS']].sum()

organic_preference = final_df.groupby('NATURAL_ORGANIC_FLAG')[['SPEND', 'UNITS']].sum()

