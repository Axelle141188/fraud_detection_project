# Banking Fraud Detection through Data Analysis

## Overview
This project develops a banking fraud detection system using machine learning techniques to identify suspicious transactions with a detection rate above 85% while maintaining a low false positive rate (<1%). The approach combines in-depth exploratory analysis, feature engineering, and comparison of different algorithms to find the optimal solution with quantified business impact.

## Project Structure
```
fraud_detection_project/
├── README.md                              # Project overview and documentation
├── requirements.txt                       # Python dependencies
├── data/
│   ├── raw/                              # Original raw data
│   │   └── creditcard.csv                # Original transaction dataset
│   └── processed/                        # Data prepared for modeling
│       ├── creditcard_processed.csv      # Dataset with transformed features
│       └── prepared_data.pkl             # Formatted data for training/testing
├── notebooks/
│   ├── 01_data_exploration.ipynb         # Initial exploratory analysis
│   ├── 02_data_preparation.ipynb         # Preprocessing and feature engineering
│   ├── 03_model_development.ipynb        # Model development and comparison
│   ├── 04_model_evaluation.ipynb         # In-depth evaluation and fine-tuning
│   └── 05_insights_and_recommendations.ipynb # Impact analysis and business insights
├── models/
│   └── fraud_detection_model.pkl         # Best trained model
├── visualizations/
│   ├── exploratory/                      # Exploratory analysis visualizations
│   └── results/                          # Model results visualizations
├── src/
│   ├── __init__.py
│   ├── data_processing.py                # Data processing functions
│   ├── feature_engineering.py            # Feature creation functions
│   ├── model_utils.py                    # Model utilities
│   └── evaluation_metrics.py             # Custom metric functions
└── presentation/
    ├── fraud_detection_slides.pdf        # Project results presentation
    └── images/                           # Images for presentation
```

## Dataset
The project uses the "Credit Card Fraud Detection" dataset from Kaggle, which contains credit card transactions with fraudulent cases:

- **284,807 total transactions**
- **492 frauds (0.172% of transactions)** - realistic extreme class imbalance
- **31 columns** with 28 anonymized via PCA (to protect confidentiality)
- Variables V1-V28 are principal components obtained via PCA
- The 'Time' and 'Amount' variables are the only non-transformed ones

## Methodology
The project follows a structured approach in five main phases:

### 1. Data Exploration
- Analysis of distributions and descriptive statistics
- Identification of temporal fraud patterns (peak fraud hours: 1-3 AM with 9.9x higher risk)
- Study of correlations between variables
- Visualization of distribution differences between normal and fraudulent transactions

### 2. Data Preparation
- Variable transformation (normalization, creation of cyclical features for time)
- Handling class imbalance via different techniques:
  - SMOTE (Synthetic Minority Over-sampling Technique)
  - Combination of SMOTE and undersampling
- Feature engineering including outlier detection and temporal analysis

### 3. Model Development
- Implementation and comparison of several algorithms:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Each model tested with different class rebalancing strategies
- Analysis of precision/recall trade-offs for each approach

### 4. Evaluation
- Business-optimized threshold selection to maximize net benefit
- Analysis of false positive and false negative cases
- Identification of the most important variables via SHAP analysis
- ROC curves and AUC to evaluate overall model performance
- Comprehensive business impact assessment

### 5. Impact Analysis
- Quantification of the financial impact of the model
- ROI calculation and potential savings estimation
- Formulation of business recommendations based on identified patterns

## Key Results

**Model Performance:**
- The best model (Random Forest + SMOTE) achieves a **detection rate of 88.8%** with **0.65% false positives**
- AUC-ROC: 0.943 (excellent discrimination capability)
- Precision: 19.1% (excellent for fraud detection context)
- F1-Score: 0.314
- **Optimal threshold: 0.840** (business-optimized)

**Business Impact:** *(Note: Cost parameters are realistic estimates for demonstration)*
- **Monthly Net Benefit: €111,375**
- **Annual Savings Estimate: €1,336,500**
- **ROI: 50.3%** return on investigation investment
- **Cost Efficiency: €1.5** saved per €1 invested

**Pattern Discovery:**
- **Temporal Patterns:** Fraud risk increases 9.9x during 1-3 AM hours
- **Amount Patterns:** Small transactions (€0-€10) show higher fraud rates
- **Most Important Features:** V14, V4, V12, Amount, Hour (via SHAP analysis)

**Operational Insights:**
- False positives: 369 alerts (0.65% of legitimate transactions) - manageable workload
- False negatives: 11 missed frauds (11.2% of frauds) - acceptable business risk
- Dynamic threshold potential based on temporal patterns

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
```

### Usage
The notebooks can be executed in order to reproduce the complete analysis:
```bash
jupyter notebook notebooks/
```

To directly use the trained model:
```python
from src.model_utils import load_model

# Load the model
model = load_model('models/fraud_detection_model.pkl')

# Make predictions on new data
predictions = model.predict(new_data)
probabilities = model.predict_proba(new_data)[:, 1]
```

## Business Recommendations

Based on the results obtained, here are the main recommendations:

### 1. Deploy real-time detection system
Implement the model with optimal threshold of 0.840 for maximum business benefit.
- **Priority:** High
- **Estimated Impact:** High  
- **Complexity:** Medium

### 2. Enhanced monitoring during high-risk hours
Implement increased surveillance of transactions during 1-3 AM period (9.9x higher fraud risk).
- **Priority:** High
- **Estimated Impact:** Medium
- **Complexity:** Low

### 3. Additional verification for small amounts
Enhanced scrutiny for small amount transactions showing elevated fraud patterns.
- **Priority:** Medium
- **Estimated Impact:** Medium
- **Complexity:** Low

### 4. Real-time monitoring dashboard
Develop operational dashboard with SHAP explanations for fraud analysts.
- **Priority:** Medium
- **Estimated Impact:** Medium
- **Complexity:** Medium

### 5. Quarterly model retraining
Regular model updates to adapt to evolving fraud patterns.
- **Priority:** Medium
- **Estimated Impact:** High
- **Complexity:** High

## Implementation Roadmap

- **Phase 1 (2-3 weeks):** Pilot deployment with 0.840 threshold validation
- **Phase 2 (1 month):** Limited production with 50% transaction coverage  
- **Phase 3 (2 months):** Full deployment with real-time dashboard
- **Phase 4 (Ongoing):** Continuous optimization and retraining

## Key Discussion Points

### 1. Threshold Optimization
How business cost modeling (€150 fraud cost, €20 investigation cost) led to 0.840 optimal threshold vs traditional 0.5

### 2. Business vs Technical Metrics
Why 19.1% precision is acceptable when 88.8% recall prevents €332K monthly losses

### 3. Temporal Pattern Implementation
Leveraging 9.9x fraud risk multiplier for dynamic threshold adjustment

## Limitations

- Business cost parameters are realistic estimates for demonstration purposes
- Actual implementation requires validation with institution-specific operational data
- Model performance may vary with different fraud patterns and time periods

## Author
Axelle Tandissa Inesa

## License
This project is licensed under the MIT License.
