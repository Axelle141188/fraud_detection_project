"""
Evaluation metrics for the fraud detection project.
"""
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

def calculate_business_impact(y_true, y_pred, avg_fraud_amount, cost_per_false_positive):
    """
    Calculate the business impact of the fraud detection model.
    
    Parameters:
    -----------
    y_true: array-like
        True labels
    y_pred: array-like
        Predicted labels
    avg_fraud_amount: float
        Average amount of a fraudulent transaction
    cost_per_false_positive: float
        Estimated cost of investigating a false positive
        
    Returns:
    --------
    dict
        Dictionary containing business impact metrics
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    # Calculate financial impact
    fraud_savings = tp * avg_fraud_amount
    false_positive_cost = fp * cost_per_false_positive
    false_negative_cost = fn * avg_fraud_amount
    net_savings = fraud_savings - false_positive_cost - false_negative_cost
    
    # Calculate rates
    fraud_detection_rate = tp / (tp + fn) if (tp + fn) > 0 else 0
    false_alarm_rate = fp / (fp + tn) if (fp + tn) > 0 else 0
    
    return {
        'true_positives': tp,
        'false_positives': fp,
        'false_negatives': fn,
        'true_negatives': tn,
        'fraud_detection_rate': fraud_detection_rate,
        'false_alarm_rate': false_alarm_rate,
        'fraud_savings': fraud_savings,
        'false_positive_cost': false_positive_cost,
        'false_negative_cost': false_negative_cost,
        'net_savings': net_savings
    }

def compare_approaches(y_true, y_pred, avg_fraud_amount, cost_per_false_positive):
    """
    Compare different fraud detection approaches.
    
    Parameters:
    -----------
    y_true: array-like
        True labels
    y_pred: array-like
        Predicted labels
    avg_fraud_amount: float
        Average amount of a fraudulent transaction
    cost_per_false_positive: float
        Estimated cost of investigating a false positive
        
    Returns:
    --------
    pd.DataFrame
        DataFrame comparing different approaches
    """
    # Calculate impact with our model
    model_impact = calculate_business_impact(y_true, y_pred, avg_fraud_amount, cost_per_false_positive)
    
    # No detection (baseline)
    no_detection_pred = np.zeros_like(y_true)
    no_detection_impact = calculate_business_impact(y_true, no_detection_pred, avg_fraud_amount, cost_per_false_positive)
    
    # Perfect detection (theoretical upper bound)
    perfect_detection_pred = y_true.copy()
    perfect_impact = calculate_business_impact(y_true, perfect_detection_pred, avg_fraud_amount, cost_per_false_positive)
    
    # Create comparison DataFrame
    comparison = pd.DataFrame({
        'No Detection': [0, no_detection_impact['false_negative_cost'], -no_detection_impact['false_negative_cost']],
        'Our Model': [model_impact['fraud_savings'], model_impact['false_positive_cost'] + model_impact['false_negative_cost'], model_impact['net_savings']],
        'Perfect Detection': [perfect_impact['fraud_savings'], 0, perfect_impact['net_savings']]
    }, index=['Savings', 'Costs', 'Net Impact'])
    
    return comparison
