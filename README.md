# Retail Analytics Dashboard

## Project Overview
This is a comprehensive retail analytics application built using Streamlit, designed to provide insights into customer behavior, purchasing trends, and product associations in a retail dataset.

## Project Structure
The project consists of several key Python scripts:

### Data Preparation and Analysis
- `data_preparation.py`: Handles data cleaning, merging, and feature engineering
  - Processes three main datasets: households, products, and transactions
  - Performs data cleaning and null value handling
  - Calculates customer engagement metrics
  - Prepares data for various analyses including spending trends, churn prediction, and basket analysis

### Streamlit Applications
1. `Home.py`: 
   - Provides an overview of the dataset
   - Allows sorting of data by different columns

2. `1_Search.py`:
   - Enables searching and filtering of data by Household Number (HSHD_NUM)
   - Provides sorting functionality

3. `2_Dashboard.py`:
   - Visualizes key insights including:
     * Demographics and Engagement
     * Household Size vs Spend
     * Impact of Children on Spending
     * Store Location Analysis
     * Spending Trends Over Time
     * Product Category Performance

4. `3_Churn_Prediction.py`:
   - Displays correlation analysis between disengagement and demographics
   - Visualizes spend and purchase frequency trends by disengagement status

5. `4_Basket_Analysis.py`:
   - Performs association rules analysis
   - Generates insights into product co-purchases
   - Allows filtering of association rules by support and confidence

### Data Retrieval
- `retrieve_data.py`: Uploads datasets to MongoDB for potential cloud storage and retrieval

## Key Features
- Comprehensive data cleaning and preprocessing
- Interactive Streamlit dashboard
- Multiple views of retail data:
  - Transaction search
  - Demographic insights
  - Spending trends
  - Churn prediction
  - Basket analysis

## Prerequisites
- Python 3.8+
- Streamlit
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn
- MLxtend
- PyMongo (for data retrieval script)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/retail-analytics-dashboard.git
cd retail-analytics-dashboard
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Run the Streamlit application
```bash
streamlit run Home.py
```

## Data Sources
The project uses three primary CSV files:
- `households.csv`: Household demographic information
- `products.csv`: Product details
- `transactions.csv`: Transaction records

## Configuration
- Ensure MongoDB connection details are set in Streamlit secrets if using the data retrieval script

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
[Specify your license here]

## Contact
[Your contact information]
