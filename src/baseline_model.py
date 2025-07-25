import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings

warnings.filterwarnings('ignore')

def main():
    print("=== House Prices Baseline Model ===\n")
    
    # 1. Load the data
    print("Loading data...")
    train_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    print(f"Training data shape: {train_df.shape}")
    print(f"Test data shape: {test_df.shape}\n")
    
    # 2. Select only numerical features
    print("Selecting numerical features...")
    
    # Get numerical columns from training data (excluding Id and SalePrice)
    numerical_features = train_df.select_dtypes(include=[np.number]).columns.tolist()
    numerical_features.remove('Id')  # Remove Id column
    numerical_features.remove('SalePrice')  # Remove target variable
    
    print(f"Found {len(numerical_features)} numerical features:")
    for i, feature in enumerate(numerical_features, 1):
        print(f"{i:2d}. {feature}")
    print()
    
    # Extract features and target
    X_train = train_df[numerical_features].copy()
    y_train = train_df['SalePrice'].copy()
    X_test = test_df[numerical_features].copy()
    
    # 3. Fill missing values with median
    print("Handling missing values...")
    print("Missing values before imputation:")
    train_missing = X_train.isnull().sum()
    test_missing = X_test.isnull().sum()
    
    # Show features with missing values
    train_missing_features = train_missing[train_missing > 0]
    test_missing_features = test_missing[test_missing > 0]
    
    if len(train_missing_features) > 0:
        print("Train set missing values:")
        for feature, count in train_missing_features.items():
            print(f"  {feature}: {count}")
    
    if len(test_missing_features) > 0:
        print("Test set missing values:")
        for feature, count in test_missing_features.items():
            print(f"  {feature}: {count}")
    
    # Fill missing values with median
    for feature in numerical_features:
        if X_train[feature].isnull().sum() > 0 or X_test[feature].isnull().sum() > 0:
            median_value = X_train[feature].median()
            X_train[feature].fillna(median_value, inplace=True)
            X_test[feature].fillna(median_value, inplace=True)
    
    print(f"Missing values after imputation: {X_train.isnull().sum().sum()} (train), {X_test.isnull().sum().sum()} (test)")
    print()
    
    # 4. Train LinearRegression model
    print("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on training set for evaluation
    y_train_pred = model.predict(X_train)
    
    # Calculate training metrics
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    train_r2 = r2_score(y_train, y_train_pred)
    
    print(f"Training RMSE: ${train_rmse:,.2f}")
    print(f"Training R²: {train_r2:.4f}")
    print()
    
    # 5. Make predictions on test set
    print("Making predictions on test set...")
    y_test_pred = model.predict(X_test)
    
    # Ensure no negative predictions
    y_test_pred = np.maximum(y_test_pred, 0)
    
    print(f"Test predictions range: ${y_test_pred.min():,.0f} - ${y_test_pred.max():,.0f}")
    print(f"Test predictions mean: ${y_test_pred.mean():,.0f}")
    print()
    
    # 6. Create submission file in Kaggle format
    print("Creating submission file...")
    submission = pd.DataFrame({
        'Id': test_df['Id'],
        'SalePrice': y_test_pred
    })
    
    submission.to_csv('submission.csv', index=False)
    print("Submission file 'submission.csv' created successfully!")
    print(f"Submission shape: {submission.shape}")
    print("\nFirst 10 predictions:")
    print(submission.head(10).to_string(index=False))
    
    # Show feature importance (coefficients)
    print(f"\nTop 10 most important features (by absolute coefficient):")
    feature_importance = pd.DataFrame({
        'feature': numerical_features,
        'coefficient': model.coef_
    })
    feature_importance['abs_coefficient'] = np.abs(feature_importance['coefficient'])
    feature_importance = feature_importance.sort_values('abs_coefficient', ascending=False)
    
    for i, (_, row) in enumerate(feature_importance.head(10).iterrows(), 1):
        print(f"{i:2d}. {row['feature']:15} : {row['coefficient']:10.2f}")
    
    print(f"\nModel intercept: {model.intercept_:.2f}")
    print("\n=== Baseline Model Complete ===")

if __name__ == "__main__":
    main()