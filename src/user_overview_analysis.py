
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def explore_data(data):
    print("Data Info:")
    print(data.info())
    
    print("\nFirst Few Rows:")
    print(data.head())
    
    print("\nDescriptive Statistics:")
    print(data.describe())

if __name__ == "__main__":
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'
    data = load_data(file_path)
    explore_data(data)

