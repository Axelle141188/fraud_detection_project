# Processed Data

This directory contains the processed datasets after feature engineering:

## Files
- `creditcard_processed.csv`: Full dataset after preprocessing
- `prepared_data.pkl`: Python pickle file containing:
  - Train-test split (X_train, X_test, y_train, y_test)
  - SMOTE resampled data (X_train_smote, y_train_smote)
  - Combined resampling data (X_train_combined, y_train_combined)

## Processing applied
- Feature engineering (time converted to cyclical features)
- Log transformation of amount
- Outlier detection
- Standardization using StandardScaler
- Class imbalance handling with SMOTE and undersampling
