"""
Model utilities for the fraud detection project.
"""
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, precision_recall_curve

def save_model(model, filepath):
    """
    Save a trained model to disk.
    
    Parameters:
    -----------
    model: sklearn model
        Trained model to save
    filepath: str
        Path where to save the model
    """
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {filepath}")

def load_model(filepath):
    """
    Load a trained model from disk.
    
    Parameters:
    -----------
    filepath: str
        Path to the saved model
        
    Returns:
    --------
    Model object
        Loaded model
    """
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

def find_optimal_threshold(y_true, y_proba, metric='f1', return_curve=False):
    """
    Find the optimal threshold for classification based on a given metric.
    
    Parameters:
    -----------
    y_true: array-like
        True labels
    y_proba: array-like
        Predicted probabilities for the positive class
    metric: str
        Metric to optimize ('f1', 'precision', 'recall')
    return_curve: bool
        Whether to return the full curve data
        
    Returns:
    --------
    float or tuple
        Optimal threshold or tuple with threshold and curve data
    """
    thresholds = np.arange(0, 1, 0.01)
    scores = []
    
    for threshold in thresholds:
        y_pred = (y_proba >= threshold).astype(int)
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
        
        if metric == 'f1':
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        elif metric == 'recall':
            score = tp / (tp + fn) if (tp + fn) > 0 else 0
        elif metric == 'precision':
            score = tp / (tp + fp) if (tp + fp) > 0 else 0
        
        scores.append(score)
    
    best_idx = np.argmax(scores)
    best_threshold = thresholds[best_idx]
    
    if return_curve:
        return best_threshold, thresholds, scores
    return best_threshold
