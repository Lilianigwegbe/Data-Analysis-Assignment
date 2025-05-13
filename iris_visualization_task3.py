import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris(as_frame=True)
iris_df = iris.frame

# Map target values to species names
target_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_df['species'] = iris_df['target'].map(target_names)

# --- Task 3: Data Visualization (Customized) ---

print("\n--- Task 3: Data Visualization (Customized) ---")

# Use seaborn style for better aesthetics
sns.set_style("whitegrid")

# 1. Line Chart (adapted and customized)
plt.figure(figsize=(10, 6))
species_means = iris_df.groupby('species')['petal length (cm)'].mean().sort_values()
sns.lineplot(x=species_means.index, y=species_means.values, marker='o', color='teal')
plt.title('Average Petal Length per Species (Sorted)', fontsize=16)
plt.xlabel('Species (Sorted by Average Petal Length)', fontsize=12)
plt.ylabel('Average Petal Length (cm)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2. Bar Chart (customized with seaborn)
plt.figure(figsize=(10, 6))
avg_petal_length = iris_df.groupby('species')['petal length (cm)'].mean()
sns.barplot(x=avg_petal_length.index, y=avg_petal_length.values, palette='viridis')
plt.title('Average Petal Length per Species', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Average Petal Length (cm)', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# 3. Histogram (customized with seaborn)
plt.figure(figsize=(10, 6))
sns.histplot(iris_df['sepal width (cm)'], bins=10, kde=True, color='salmon')
plt.title('Distribution of Sepal Width', fontsize=16)
plt.xlabel('Sepal Width (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', alpha=0.7)
plt.tight_layout()
plt.show()

# 4. Scatter Plot (customized with seaborn)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df, palette='Set2', s=80)
plt.title('Sepal Length vs. Petal Length', fontsize=16)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Petal Length (cm)', fontsize=12)
plt.legend(title='Species', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

