import pandas as pd
import numpy as np

# Load data
train_df = pd.read_csv('train.csv')

# Calculate outlier threshold using IQR method
Q1 = train_df['GrLivArea'].quantile(0.25)
Q3 = train_df['GrLivArea'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = train_df[(train_df['GrLivArea'] < lower_bound) | (train_df['GrLivArea'] > upper_bound)]

print(f"Number of outliers in GrLivArea: {len(outliers)}")
print(f"Outlier threshold: {upper_bound:.0f} sq ft")
print("\nOutlier details:")
outlier_details = outliers[['Id', 'GrLivArea', 'SalePrice']].sort_values('GrLivArea', ascending=False)
print(outlier_details.to_string(index=False))