import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def load_data(file_path):
    """
    Loads the dataset from the given file path.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    print(f"Loading data from {file_path}...")
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    return data

def aggregate_user_engagement(data):
    """
    Aggregates user engagement metrics including session count, average session duration, and total data volume.
    Args:
        data (pd.DataFrame): The dataset.
    Returns:
        pd.DataFrame: Aggregated user engagement data.
    """
    user_metrics = data.groupby('MSISDN/Number').agg({
        'Dur. (ms)': ['count', 'mean', 'sum'],  
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum'
    }).reset_index()

   
    user_metrics.columns = ['User ID', 'Session Count', 'Avg Session Duration', 'Total Session Duration',
                            'Total DL (Bytes)', 'Total UL (Bytes)']

    user_metrics['Total Data Volume'] = user_metrics['Total DL (Bytes)'] + user_metrics['Total UL (Bytes)']

    print("\nAggregated User Engagement Metrics:")
    print(user_metrics.head())
    return user_metrics

def main():
    
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'

    
    data = load_data(file_path)
    user_metrics = aggregate_user_engagement(data)

   

if __name__ == "__main__":
    main()
