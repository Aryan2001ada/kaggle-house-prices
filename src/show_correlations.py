import pandas as pd
import numpy as np

# Load data
train_df = pd.read_csv('train.csv')

# Get correlation data
numeric_features = train_df.select_dtypes(include=[np.number])
corr_with_target = numeric_features.corr()['SalePrice'].abs().sort_values(ascending=False)
top_3_features = corr_with_target.drop('SalePrice').head(3).index.tolist()

print(f"Top 3 features most correlated with SalePrice: {top_3_features}")
print(f"Correlation values: {corr_with_target[top_3_features].values}")

# Show correlation coefficients
for i, feature in enumerate(top_3_features):
    corr_coef = train_df[feature].corr(train_df['SalePrice'])
    print(f"{i+1}. {feature}: {corr_coef:.3f}")