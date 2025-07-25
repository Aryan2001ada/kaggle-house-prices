# Data Directory

This directory is designated for the dataset files from the **House Prices: Advanced Regression Techniques** Kaggle competition.

## 📊 Data Source

The dataset comes from the Kaggle competition:
**[House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)**

### 📥 How to Download the Data

1. **Visit the competition page**: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
2. **Sign in** to your Kaggle account (create one if needed)
3. **Accept the competition rules** by clicking "Join Competition"
4. **Download the data files** from the Data tab
5. **Place the CSV files** in the root directory of this project (one level up from this folder)

Alternatively, use the Kaggle API:
```bash
pip install kaggle
kaggle competitions download -c house-prices-advanced-regression-techniques
unzip house-prices-advanced-regression-techniques.zip
```

## 📁 Required Data Files

The following files should be placed in the **root directory** (not in this data folder):

### `train.csv` (460 KB)
- **1,460 samples** × **81 features** (including target)
- Contains all house features **plus** the target variable `SalePrice`
- Used for **training** machine learning models
- Each row represents one house sale

### `test.csv` (451 KB)  
- **1,459 samples** × **80 features** (no target)
- Contains all house features **without** the target variable
- Used for making **final predictions** for Kaggle submission
- Same feature structure as training data (minus SalePrice)

### `sample_submission.csv` (31 KB)
- **Template** showing the required submission format
- Contains `Id` and `SalePrice` columns
- Shows the expected structure for Kaggle submissions

### `data_description.txt`
- **Detailed documentation** of all 79 explanatory variables
- Explains data types, possible values, and meanings
- Essential reference for understanding the dataset

## 🚫 Important Note

**Raw data files are not included in this GitHub repository** for the following reasons:
- **File size**: CSV files are large and not suitable for version control
- **Kaggle terms**: Competition data should be downloaded directly from Kaggle
- **Freshness**: Ensures you always get the latest version from the official source
- **Best practice**: Raw data stays separate from code in data science projects

## 📋 Dataset Overview

- **Competition Type**: Regression (predict continuous house prices)
- **Target Variable**: `SalePrice` (house sale price in dollars)
- **Feature Count**: 79 explanatory variables
- **Data Types**: Mix of numerical and categorical features
- **Missing Values**: Present in multiple features (handled in preprocessing)
- **Time Period**: House sales in Ames, Iowa (2006-2010)

## 🏠 What the Data Represents

This dataset describes residential homes in **Ames, Iowa** with features covering:
- **Property details**: Lot size, building type, zoning
- **House structure**: Square footage, rooms, bathrooms
- **Quality ratings**: Overall condition, material quality
- **Amenities**: Garage, pool, deck, porch details
- **Location**: Neighborhood information
- **Sale details**: Sale type, date, conditions

## 🔧 Usage in This Project

The data files are referenced by scripts and notebooks located in:
- `src/` - Python scripts for data processing
- `notebooks/` - Jupyter notebooks for analysis and modeling

All code assumes the CSV files are in the root directory for easy access.