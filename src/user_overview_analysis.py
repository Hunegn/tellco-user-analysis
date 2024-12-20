
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
def handsets(data):
    top_handsets = data['Handset Type'].value_counts().head(10)
    print("\nTop 10 Handsets:")
    print(top_handsets)


  
if __name__ == "__main__":
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'
    data = load_data(file_path)
    explore_data(data)
    handsets(data)
    

