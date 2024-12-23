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

def main():
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'

    data = load_data(file_path)
    clean_data(data)


if __name__ == "__main__":
    main()
