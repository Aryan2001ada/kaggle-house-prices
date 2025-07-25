import pandas as pd
import numpy as np

def main():
    print("=== House Prices Dataset Exploration ===\n")
    
    # Load datasets
    print("Loading datasets...")
    train_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    print("Datasets loaded successfully!\n")
    
    # Shape of both datasets
    print("=== Dataset Shapes ===")
    print(f"Training data shape: {train_df.shape}")
    print(f"Test data shape: {test_df.shape}\n")
    
    # First 5 rows of training data
    print("=== First 5 Rows of Training Data ===")
    print(train_df.head())
    print("\n")
    
    # Data types of all columns
    print("=== Data Types ===")
    print("Training data column types:")
    print(train_df.dtypes)
    print("\n")
    
    # Missing value counts for each column
    print("=== Missing Values Count ===")
    print("Training data missing values:")
    train_missing = train_df.isnull().sum()
    train_missing = train_missing[train_missing > 0].sort_values(ascending=False)
    if len(train_missing) > 0:
        print(train_missing)
    else:
        print("No missing values in training data")
    
    print("\nTest data missing values:")
    test_missing = test_df.isnull().sum()
    test_missing = test_missing[test_missing > 0].sort_values(ascending=False)
    if len(test_missing) > 0:
        print(test_missing)
    else:
        print("No missing values in test data")
    print("\n")
    
    # Basic statistics of SalePrice
    print("=== SalePrice Statistics ===")
    print(train_df['SalePrice'].describe())
    print(f"\nSalePrice range: ${train_df['SalePrice'].min():,.0f} - ${train_df['SalePrice'].max():,.0f}")
    print(f"SalePrice mean: ${train_df['SalePrice'].mean():,.0f}")
    print(f"SalePrice median: ${train_df['SalePrice'].median():,.0f}")

if __name__ == "__main__":
    main()