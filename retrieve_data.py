import pandas as pd
from pymongo import MongoClient
import streamlit as st

households_df = pd.read_csv('./datasets/households.csv')
products_df = pd.read_csv('./datasets/products.csv')
transaction_df = pd.read_csv('./datasets/transactions.csv')


households_df_dict = households_df.to_dict(orient='records')
products_df_dict = products_df.to_dict(orient='records')
transaction_df_dict = transaction_df.to_dict(orient='records')


client = MongoClient(st.secrets['MONGO_URL'])
db = client['machinelearning']
households_df_collection = db['households_df_collection']
products_df_collection = db['products_df_collection']
transaction_df_collection = db['transaction_df_collection']

# Insert the data into MongoDB
households_df_collection.insert_many(households_df_dict)

products_df_collection.insert_many(products_df_dict)

transaction_df_collection.insert_many(transaction_df_dict)

print("CSV data uploaded successfully to MongoDB!")

