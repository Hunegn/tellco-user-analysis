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

def aggregate_customer_data(data):
    """
    Aggregates network parameters and handset type per customer.
    """
   
    numeric_cols = ['TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)',
                    'Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']
    for col in numeric_cols:
        data[col].fillna(data[col].mean(), inplace=True)


    aggregated_data = data.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'TCP UL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Avg RTT UL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Avg Bearer TP UL (kbps)': 'mean',
        'Handset Type': 'first'
    }).reset_index()

    aggregated_data.rename(columns={
        'TCP DL Retrans. Vol (Bytes)': 'Avg TCP Retransmission',
        'TCP UL Retrans. Vol (Bytes)': 'Avg TCP Retransmission UL',
        'Avg RTT DL (ms)': 'Avg RTT DL',
        'Avg RTT UL (ms)': 'Avg RTT UL',
        'Avg Bearer TP DL (kbps)': 'Avg Throughput DL',
        'Avg Bearer TP UL (kbps)': 'Avg Throughput UL'
    }, inplace=True)

    print("\nAggregated Customer Data:")
    print(aggregated_data.head())
    return aggregated_data

def analyze_parameters(data):
    """
    Computes and lists top, bottom, and most frequent values for TCP, RTT, and Throughput.
    """
    parameters = ['Avg TCP Retransmission', 'Avg RTT DL', 'Avg Throughput DL']

    for param in parameters:
        print(f"\nAnalysis for {param}:")
        print(f"Top 10:\n{data[param].nlargest(10)}")
        print(f"Bottom 10:\n{data[param].nsmallest(10)}")
        print(f"Most Frequent:\n{data[param].mode().values[0]}")


def main():
    file_path = '../data/Copy of Week2_challenge_data_source(CSV).csv'

    data = load_data(file_path)
    aggregated_data = aggregate_customer_data(data)
    analyze_parameters(aggregated_data)


if __name__ == "__main__":
    main()
