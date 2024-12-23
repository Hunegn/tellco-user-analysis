import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
def clean_data(data):
    """
    Cleans the dataset by handling missing values and outliers.
    Args:
        data (pd.DataFrame): The dataset.
    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    print('Data before cleaning rows: ', len(data))
    
    data = data.dropna(subset=['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)'])
  
   
    for col in ['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']:
        data = data[data[col] >= 0]  
    
    print("\nData cleaned. Remaining rows:", len(data))
    return data
def correlation_analysis(data):
    """
    Analyzes correlations between network parameters and user metrics.
    Args:
        data (pd.DataFrame): The dataset.
    """
    correlation_columns = ['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)',
                           'Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']
    corr_matrix = data[correlation_columns].corr()
    
   
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix of Network Parameters and User Metrics")
    plt.show()
def scatter_plots(data):
    """
    Creates scatter plots to explore relationships between network parameters and user metrics.
    Args:
        data (pd.DataFrame): The dataset.
    """
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='Avg RTT DL (ms)', y='Dur. (ms)', alpha=0.6, color='blue')
    plt.title("RTT (Download) vs. Session Duration")
    plt.xlabel("Avg RTT DL (ms)")
    plt.ylabel("Session Duration (ms)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
   
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='Avg Bearer TP DL (kbps)', y='Total DL (Bytes)', alpha=0.6, color='green')
    plt.title("Throughput (Download) vs. Data Volume")
    plt.xlabel("Avg Bearer TP DL (kbps)")
    plt.ylabel("Total Download Volume (Bytes)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def main():
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'

    data = load_data(file_path)
    clean_data(data)
    correlation_analysis(data)
    scatter_plots(data)


if __name__ == "__main__":
    main()
