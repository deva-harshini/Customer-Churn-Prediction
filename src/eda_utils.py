# src/eda_utils.py

def churn_rate(df, column):
    """
    Calculate normalized churn rate for a categorical column
    """
    return df.groupby(column, observed=True)['Churn'].value_counts(normalize=True).unstack()
