"""
Data processing utilities for the fraud detection project.
"""
import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load the raw transaction data.
    
    Parameters:
    -----------
    filepath: str
        Path to the raw data file
    
    Returns:
    --------
    pd.DataFrame
        Loaded data
    """
    df = pd.read_csv(filepath)
    print(f"Loaded data with {df.shape[0]} rows and {df.shape[1]} columns")
    return df

def check_missing_values(df):
    """
    Check for missing values in the dataset.
    
    Parameters:
    -----------
    df: pd.DataFrame
        Dataset to check
    
    Returns:
    --------
    pd.Series
        Count of missing values per column
    """
    return df.isnull().sum()

def convert_time_to_hour(df, time_column='Time'):
    """
    Convert Time column (seconds) to hour of day.
    
    Parameters:
    -----------
    df: pd.DataFrame
        Dataset containing the Time column
    time_column: str
        Name of the time column
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with new Hour column
    """
    df_copy = df.copy()
    df_copy['Hour'] = df_copy[time_column].apply(lambda x: (x // 3600) % 24)
    return df_copy

def normalize_amount(df, amount_column='Amount'):
    """
    Apply log transformation and standardization to Amount column.
    
    Parameters:
    -----------
    df: pd.DataFrame
        Dataset containing the Amount column
    amount_column: str
        Name of the amount column
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with normalized Amount
    """
    df_copy = df.copy()
    df_copy['Amount_Log'] = np.log1p(df_copy[amount_column])
    return df_copy
