import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris(as_frame=True)
iris_df = iris.frame

# Task 2: Basic Data Analysis

# Step 1: Compute basic statistics of numerical columns
print("\n--- Task 2: Basic Data Analysis ---")
print("\nBasic statistics of the numerical columns:")
print(iris_df.describe())

# Step 2: Perform groupings on a categorical column and compute the mean of a numerical column for each group
# The 'target' column is categorical (representing species). Let's map the numerical values to their names for better readability.
target_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_df['species'] = iris_df['target'].map(target_names)

print("\nMean of numerical features grouped by species:")
mean_by_species = iris_df.groupby('species').mean()
print(mean_by_species)

# Step 3: Identify any patterns or interesting findings from your analysis
print("\n--- Interesting Findings ---")

print("\n1. Feature Distributions (from .describe()):")
print("- Sepal Length has a wider range and higher average than Sepal Width.")
print("- Petal Length and Petal Width have significantly larger ranges and averages compared to the sepal dimensions.")
print("- The standard deviations suggest varying degrees of spread within each feature.")

print("\n2. Grouped Means by Species:")
print("- Setosa generally has the smallest sepal length, sepal width, petal length, and petal width on average.")
print("- Virginica tends to have the largest sepal length, petal length, and petal width on average.")
print("- Versicolor falls in between Setosa and Virginica for most features.")
print("- The differences in petal length and petal width means across the species appear more pronounced than the differences in sepal dimensions, suggesting these features might be more important in distinguishing the species.")

print("\n3. Potential Patterns:")
print("- There seems to be a clear separation in the average feature measurements across the three Iris species.")
print("- Petal dimensions (length and width) might be stronger indicators of species compared to sepal dimensions.")

# Note: More in-depth pattern identification would typically involve visualizations (Task 3)
# to see the distributions and relationships more clearly.
