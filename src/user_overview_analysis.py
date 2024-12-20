
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def inspect_data(data):
    print("Data Info:")
    print(data.info())
    
    print("\nFirst Few Rows:")
    print(data.head())
    print("\nMissing Values:")
    
    print(data.isnull().sum())
    print("\nDescriptive Statistics:")
    
    print(data.describe())
def top_10_handsets(data):
    top_handsets = data['Handset Type'].value_counts().head(10)
    print("\nTop 10 Handsets:")
    print(top_handsets)

def top_3_manufacturers(data):
    top_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    print("\nTop 3 Manufacturers:")
    print(top_manufacturers)
    return top_manufacturers.index
def top_5_handsets_per_manufacturer(data, top_manufacturers):
    """
    Finds the top 5 handsets for each of the top 3 manufacturers.
    Args:
        data (pd.DataFrame): The dataset.
        top_manufacturers (pd.Index): Names of the top 3 manufacturers.
    """
    for manufacturer in top_manufacturers:
        print(f"\nTop 5 Handsets for {manufacturer}:")
        handsets = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        print(handsets)
  
if __name__ == "__main__":
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'
    data = load_data(file_path)
    #inspect_data(data)
    top_10_handsets(data)
    top_3_manufacturers(data)
    top_manufacturers = top_3_manufacturers(data)
    top_5_handsets_per_manufacturer(data, top_manufacturers)
    

