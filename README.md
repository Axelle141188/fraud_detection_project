# Banking Fraud Detection through Data Analysis

## Overview
This project develops a banking fraud detection system using machine learning techniques to identify suspicious transactions with a detection rate above 80% while maintaining an extremely low false positive rate (0.1%). The approach combines in-depth exploratory analysis, feature engineering, and comparison of different algorithms to find the optimal solution.

## Project Structure
fraud_detection_project/
├── README.md                           # Project overview and documentation
├── requirements.txt                    # Python dependencies
├── data/
│   ├── raw/                            # Original raw data
│   │   └── creditcard.csv              # Original transaction dataset
│   └── processed/                      # Data prepared for modeling
│       ├── creditcard_processed.csv    # Dataset with transformed features
│       └── prepared_data.pkl           # Formatted data for training/testing
├── notebooks/
│   ├── 01_data_exploration.ipynb       # Initial exploratory analysis
│   ├── 02_data_preparation.ipynb       # Preprocessing and feature engineering
│   ├── 03_model_development.ipynb      # Model development and comparison
│   ├── 04_model_evaluation.ipynb       # In-depth evaluation and fine-tuning
│   └── 05_insights_and_recommendations.ipynb  # Impact analysis and business insights
├── models/
│   └── fraud_detection_model.pkl       # Best trained model
├── visualizations/
│   ├── exploratory/                    # Exploratory analysis visualizations
│   └── results/                        # Model results visualizations
├── src/
│   ├── init.py
│   ├── data_processing.py              # Data processing functions
│   ├── feature_engineering.py          # Feature creation functions
│   ├── model_utils.py                  # Model utilities
│   └── evaluation_metrics.py           # Custom metric functions
└── presentation/
├── fraud_detection_slides.pdf      # Project results presentation
└── images/                         # Images for presentation

## Dataset
The project uses the "Credit Card Fraud Detection" dataset, which contains credit card transactions, some of which are fraudulent:
- 284,807 total transactions
- 492 frauds (0.172% of transactions) - a realistic imbalance
- 31 columns with 28 anonymized via PCA (to protect confidentiality)
- Variables V1-V28 are principal components obtained via PCA
- The 'Time' and 'Amount' variables are the only non-transformed ones

## Methodology
The project follows a structured approach in five main phases:

### 1. Data Exploration
- Analysis of distributions and descriptive statistics
- Identification of temporal fraud patterns (nighttime peaks at 2 AM and 4 AM)
- Study of correlations between variables
- Visualization of distribution differences between normal and fraudulent transactions

### 2. Data Preparation
- Variable transformation (normalization, creation of cyclical features for time)
- Handling class imbalance via different techniques:
  - SMOTE (Synthetic Minority Over-sampling Technique)
  - Combination of SMOTE and undersampling

### 3. Model Development
- Implementation and comparison of several algorithms:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Each model tested with different class rebalancing strategies
- Analysis of precision/recall trade-offs for each approach

### 4. Evaluation
- Optimization of the decision threshold to maximize recall while limiting false positives
- Analysis of false positive and false negative cases
- Identification of the most important variables via SHAP analysis
- ROC curves and AUC to evaluate overall model performance

### 5. Impact Analysis
- Quantification of the financial impact of the model
- ROI calculation and potential savings
- Formulation of business recommendations based on identified patterns

## Key Results
- The best model achieves a detection rate (recall) of 84.7% with only 0.1% false positives
- The best models (Gradient Boosting and XGBoost with combined strategy) achieve an AUC > 0.98
- Optimal threshold determined at 0.99 to maximize F1-score
- Most important variables identified by SHAP: Amount, V4, V10, V14, and Outlier_Count
- Analysis of false positives and false negatives revealing distinct patterns:
  - False positives mainly concern small transactions
  - False negatives are more uniformly distributed
- Identification of specific fraud patterns:
  - More frequent frauds between 2 AM and 4 AM (up to 1.7% of transactions)
  - Low amount transactions (0-10$) showing a significantly higher fraud rate (25%)
  - Certain variables (V1, V3, V4, V5, V10) particularly discriminating

## Installation and Usage

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/username/fraud_detection_project.git
cd fraud_detection_project

# Install dependencies
pip install -r requirements.txt
Usage
The notebooks can be executed in order to reproduce the complete analysis:
bashjupyter notebook notebooks/
To directly use the trained model:
pythonfrom src.model_utils import load_model

# Load the model
model = load_model('models/fraud_detection_model.pkl')

# Make predictions on new data
predictions = model.predict(new_data)
probabilities = model.predict_proba(new_data)[:, 1]
Business Recommendations
Based on the results obtained, here are the main recommendations:

Implement a real-time alert system: Deploy the model with an optimal threshold of 99.0% for effective fraud detection.

Priority: High
Estimated Impact: High
Complexity: Medium


Strengthen monitoring during high-risk hours: Implement increased surveillance of transactions made during nighttime hours, particularly between 2 AM and 4 AM.

Priority: High
Estimated Impact: Medium
Complexity: Low


Additional verification for small amount transactions: Implement an additional verification process for 0-10$ transactions, which show an abnormally high fraud rate.

Priority: Medium
Estimated Impact: Medium
Complexity: Low


Create a monitoring dashboard: Develop a dashboard similar to our prototype for fraud analysts.

Priority: Medium
Estimated Impact: Low
Complexity: Medium


Periodic model review: Re-evaluate and retrain the model every 3 months to adapt to evolving fraud patterns.

Priority: Low
Estimated Impact: High
Complexity: High



Author
[Axelle Tandissa Inesa]
License
This project is licensed under the MIT License. 
