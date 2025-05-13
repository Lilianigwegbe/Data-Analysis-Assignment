import pandas as pd
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

# Step 1 & 2: Load the Iris dataset using pandas
iris = load_iris(as_frame=True)
iris_df = iris.frame
print("Iris dataset loaded as a Pandas DataFrame.")

# Step 3: Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(iris_df.head())

# Step 4: Explore the structure
print("\nInformation about the dataset:")
iris_df.info()

print("\nNumber of missing values per column:")
print(iris_df.isnull().sum())

# Step 5: Clean the dataset (handle missing values)
if iris_df.isnull().sum().any():
    print("\nMissing values found. Deciding on a strategy to handle them...")
    # For demonstration purposes (though unlikely in Iris):
    # Let's fill numerical missing values with the mean
    for col in iris_df.columns[:-1]: # Exclude the 'target' column
        if iris_df[col].dtype in ['int64', 'float64']:
            iris_df[col].fillna(iris_df[col].mean(), inplace=True)
    print("Missing numerical values filled with the mean.")
else:
    print("\nNo missing values found in the dataset. No cleaning needed for missing values.")

print("\nFirst 5 rows after (potential) cleaning:")
print(iris_df.head())

print("\nShape of the cleaned dataset:")
print(iris_df.shape)