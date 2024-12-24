import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


def calculate_scores(data, engagement_clusters, experience_clusters):
    """
    Calculate engagement and experience scores based on Euclidean distance to clusters.
    Args:
        data (pd.DataFrame): The dataset.
        engagement_clusters (ndarray): Cluster centers from engagement analysis.
        experience_clusters (ndarray): Cluster centers from experience analysis.
    Returns:
        pd.DataFrame: Data with engagement and experience scores.
    """
    
    data['Session Count'] = data.groupby('MSISDN/Number')['Bearer Id'].transform('count')
    data['Avg Session Duration'] = data.groupby('MSISDN/Number')['Dur. (ms)'].transform('mean')
    data['Total Data Volume'] = data.groupby('MSISDN/Number')['Total DL (Bytes)'].transform('sum') + \
                                data.groupby('MSISDN/Number')['Total UL (Bytes)'].transform('sum')

    engagement_features = ['Session Count', 'Avg Session Duration', 'Total Data Volume']

   
    data['Engagement Score'] = data[engagement_features].apply(
        lambda row: np.linalg.norm(row - engagement_clusters[1]), axis=1)

  
    data['Avg TCP Retransmission'] = (data['TCP DL Retrans. Vol (Bytes)'] + data['TCP UL Retrans. Vol (Bytes)']) / 2
    data['Avg RTT DL'] = data['Avg RTT DL (ms)']
    data['Avg Throughput DL'] = data['Avg Bearer TP DL (kbps)']

    experience_features = ['Avg TCP Retransmission', 'Avg RTT DL', 'Avg Throughput DL']

   
    data['Experience Score'] = data[experience_features].apply(
        lambda row: np.linalg.norm(row - experience_clusters[1]), axis=1)

    return data
def calculate_satisfaction_score(data):
    """
    Calculate the satisfaction score as the average of engagement and experience scores.
    Args:
        data (pd.DataFrame): The dataset.
    Returns:
        pd.DataFrame: Data with satisfaction scores.
    """
  
    data['Satisfaction Score'] = (data['Engagement Score'] + data['Experience Score']) / 2

   
    top_customers = data.nlargest(10, 'Satisfaction Score')[['MSISDN/Number', 'Satisfaction Score']]
    print("\nTop 10 Satisfied Customers:")
    print(top_customers)

    return data




def main():
    
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'
    data = pd.read_csv(file_path)

   
    engagement_clusters = np.array([
    [3.367763e+10, 1.959627e+07, 1.041968e+06],  # Cluster 0: Moderate Engagement
    [4.749426e+10, 1.625573e+07, 6.719899e+05],  # Cluster 1: Low Engagement (worst)
    [3.368364e+10, 2.224330e+09, 1.161338e+06],  # Cluster 2: High Engagement (best)
    ])

    experience_clusters = np.array([
    [77.319787, 24.225670, 49171.539659],  # Cluster 0: Moderate Experience
    [126.372621, 15.220035, 3799.595727],  # Cluster 1: Low Experience (worst)
    [104.547799, 39.244130, 62838.408386],  # Cluster 2: High Experience (best)
    ])

    # Calculate engagement features
    data['Avg TCP Retransmission'] = (data['TCP DL Retrans. Vol (Bytes)'] + data['TCP UL Retrans. Vol (Bytes)']) / 2
    data['Avg RTT DL'] = data['Avg RTT DL (ms)']
    data['Avg Throughput DL'] = data['Avg Bearer TP DL (kbps)']


    # Calculate session count
    data['Session Count'] = data.groupby('MSISDN/Number')['Bearer Id'].transform('count')
    data['Avg Session Duration'] = data.groupby('MSISDN/Number')['Dur. (ms)'].transform('mean')
    data['Total Data Volume'] = data.groupby('MSISDN/Number')['Total DL (Bytes)'].transform('sum') + \
                            data.groupby('MSISDN/Number')['Total UL (Bytes)'].transform('sum')
   
    data = calculate_scores(data, engagement_clusters, experience_clusters)
    data = calculate_satisfaction_score(data)

   

if __name__ == "__main__":
    main()
