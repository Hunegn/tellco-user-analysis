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

def main():
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'

    data = load_data(file_path)
    clean_data(data)


if __name__ == "__main__":
    main()
