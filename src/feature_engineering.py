"""
Feature engineering utilities for the fraud detection project.
"""
import numpy as np
import pandas as pd
from scipy import stats

def add_cyclical_features(df, hour_column='Hour'):
    """
    Add cyclical encoding of hour to capture its circular nature.
    
    Parameters:
    -----------
    df: pd.DataFrame
        Dataset with Hour column
    hour_column: str
        Name of the hour column
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with added hour_sin and hour_cos features
    """
    df_copy = df.copy()
    df_copy['Hour_sin'] = np.sin(2 * np.pi * df_copy[hour_column]/24)
    df_copy['Hour_cos'] = np.cos(2 * np.pi * df_copy[hour_column]/24)
    return df_copy

def add_outlier_indicators(df, columns=None, z_threshold=3):
    """
    Add binary indicators for outliers in numerical features.
    
    Parameters:
    -----------
    df: pd.DataFrame
        Input dataset
    columns: list of str or None
        Columns to check for outliers. If None, uses all numeric columns
    z_threshold: float
        Z-score threshold to consider a value as outlier
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with added outlier indicator columns
    """
    df_copy = df.copy()
    
    if columns is None:
        # Use all numeric columns except the target
        columns = df.select_dtypes(include=np.number).columns
        if 'Class' in columns:
            columns = columns.drop('Class')
    
    # Create outlier flags
    for column in columns:
        z_scores = stats.zscore(df_copy[column], nan_policy='omit')
        df_copy[f'{column}_is_outlier'] = (np.abs(z_scores) > z_threshold).astype(int)
    
    # Add outlier count
    outlier_columns = [col for col in df_copy.columns if col.endswith('_is_outlier')]
    df_copy['Outlier_Count'] = df_copy[outlier_columns].sum(axis=1)
    
    return df_copy
