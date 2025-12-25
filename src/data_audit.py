# src/data_audit.py

import pandas as pd

def basic_data_audit(df: pd.DataFrame) -> dict:
    """
    Perform basic data quality checks.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe to audit

    Returns
    -------
    dict
        Dictionary containing dataset shape, missing values,
        duplicate count, and data types
    """
    audit_report = {
        "shape": df.shape,
        "missing_values": df.isnull().sum(),
        "duplicates": df.duplicated().sum(),
        "dtypes": df.dtypes
    }

    return audit_report
