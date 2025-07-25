import pandas as pd
import numpy as np
from scipy import stats

# Load data
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# Calculate missing data
all_data = pd.concat([train_df.drop('SalePrice', axis=1), test_df], axis=0, ignore_index=True)
missing_data = all_data.isnull().sum()
missing_data = missing_data[missing_data > 0].sort_values(ascending=False)

# Get top correlations
numeric_features = train_df.select_dtypes(include=[np.number])
corr_with_target = numeric_features.corr()['SalePrice'].abs().sort_values(ascending=False)
top_3_features = corr_with_target.drop('SalePrice').head(3).index.tolist()

# Outliers
Q1 = train_df['GrLivArea'].quantile(0.25)
Q3 = train_df['GrLivArea'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
outliers = train_df[train_df['GrLivArea'] > upper_bound]

print("=== EDA SUMMARY ===")
print(f"\n1. Dataset Overview:")
print(f"   - Training samples: {train_df.shape[0]:,}")
print(f"   - Features: {train_df.shape[1]-1}")
print(f"   - Test samples: {test_df.shape[0]:,}")

print(f"\n2. SalePrice Distribution:")
print(f"   - Mean: ${train_df['SalePrice'].mean():,.0f}")
print(f"   - Median: ${train_df['SalePrice'].median():,.0f}")
print(f"   - Std: ${train_df['SalePrice'].std():,.0f}")
print(f"   - Skewness: {stats.skew(train_df['SalePrice']):.3f}")
print(f"   - Log-transformed skewness: {stats.skew(np.log1p(train_df['SalePrice'])):.3f}")

print(f"\n3. Missing Data:")
print(f"   - Features with missing data: {len(missing_data)}")
print(f"   - Most missing: {missing_data.index[0]} ({missing_data.iloc[0]} values)")

print(f"\n4. Top Correlations with SalePrice:")
for i, feature in enumerate(top_3_features):
    corr_val = corr_with_target[feature]
    print(f"   {i+1}. {feature}: {corr_val:.3f}")

print(f"\n5. GrLivArea Outliers:")
print(f"   - Number of outliers: {len(outliers)}")
print(f"   - Largest outlier: {outliers['GrLivArea'].max():,.0f} sq ft")
print(f"   - These may represent luxury/commercial properties")