import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for Top 10 Handsets
handset_data = {
    'Handset Type': [
        'Huawei B528S-23A', 'Apple iPhone 6S (A1688)', 'Apple iPhone 6 (A1586)', 'undefined',
        'Apple iPhone 7 (A1778)', 'Apple iPhone Se (A1723)', 'Apple iPhone 8 (A1905)',
        'Apple iPhone Xr (A2105)', 'Samsung Galaxy S8 (Sm-G950F)', 'Apple iPhone X (A1901)'
    ],
    'Count': [19752, 9419, 9023, 8987, 6326, 5187, 4993, 4568, 4520, 3813]
}

df_handsets = pd.DataFrame(handset_data)

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(data=df_handsets, y='Handset Type', x='Count', palette='viridis')
plt.title("Top 10 Handsets by Usage", fontsize=16)
plt.xlabel("Number of Users", fontsize=12)
plt.ylabel("Handset Type", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# Data for Top 3 Manufacturers
manufacturer_data = {
    'Handset Manufacturer': ['Apple', 'Samsung', 'Huawei'],
    'Count': [59565, 40839, 34423]
}

df_manufacturers = pd.DataFrame(manufacturer_data)

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(
    df_manufacturers['Count'], 
    labels=df_manufacturers['Handset Manufacturer'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette('pastel')
)
plt.title("Top 3 Handset Manufacturers by Usage", fontsize=16)
plt.tight_layout()
plt.show()
# Data for Top 5 Handsets per Manufacturer
apple_data = {'Handset Type': [
    'Apple iPhone 6S (A1688)', 'Apple iPhone 6 (A1586)', 'Apple iPhone 7 (A1778)',
    'Apple iPhone Se (A1723)', 'Apple iPhone 8 (A1905)'],
    'Count': [9419, 9023, 6326, 5187, 4993]
}

samsung_data = {'Handset Type': [
    'Samsung Galaxy S8 (Sm-G950F)', 'Samsung Galaxy A5 Sm-A520F', 
    'Samsung Galaxy J5 (Sm-J530)', 'Samsung Galaxy J3 (Sm-J330)', 
    'Samsung Galaxy S7 (Sm-G930X)'],
    'Count': [4520, 3724, 3696, 3484, 3199]
}

huawei_data = {'Handset Type': [
    'Huawei B528S-23A', 'Huawei E5180', 'Huawei P20 Lite Huawei Nova 3E',
    'Huawei P20', 'Huawei Y6 2018'],
    'Count': [19752, 2079, 2021, 1480, 997]
}

# Function to Plot
def plot_top_5_handsets(manufacturer, data):
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, y='Handset Type', x='Count', palette='rocket')
    plt.title(f"Top 5 Handsets for {manufacturer}", fontsize=16)
    plt.xlabel("Number of Users", fontsize=12)
    plt.ylabel("Handset Type", fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Plot for Apple
plot_top_5_handsets("Apple", apple_data)

# Plot for Samsung
plot_top_5_handsets("Samsung", samsung_data)

# Plot for Huawei
plot_top_5_handsets("Huawei", huawei_data)
