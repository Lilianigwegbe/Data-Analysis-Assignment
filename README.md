# Data-Analysis-Assignment

# Data Analysis and Visualization Project

This project demonstrates fundamental data analysis and visualization techniques using the Python libraries Pandas and Matplotlib (with enhancements from Seaborn). It covers loading and exploring a dataset, performing basic statistical analysis, and creating informative visualizations.

## Project Structure

The project consists of Python scripts that address the following tasks:

* **Task 1: Load and Explore the Dataset**
* **Task 2: Basic Data Analysis**
* **Task 3: Data Visualization**

## Dataset

This project utilizes the **Iris dataset**, a classic dataset for classification problems. It contains measurements of sepal length, sepal width, petal length, and petal width for three different species of Iris flowers (setosa, versicolor, and virginica). The dataset is accessed directly using the `sklearn.datasets` module in Python, eliminating the need for a separate CSV file in this setup.

## Libraries Used

* **Pandas:** For data manipulation and analysis, particularly for loading and working with DataFrames.
* **Matplotlib:** For creating basic plots and charts.
* **Seaborn:** For enhancing the visual appeal of Matplotlib plots with additional styles and more sophisticated plotting functions.
* **Scikit-learn (`sklearn`):** For accessing the Iris dataset via `sklearn.datasets`.

## Task Descriptions and Implementation

### Task 1: Load and Explore the Dataset

* **Objective:** To load the Iris dataset and gain an initial understanding of its structure and contents.
* **Implementation:**
    * The Iris dataset is loaded using `sklearn.datasets.load_iris()` and converted into a Pandas DataFrame.
    * The first few rows of the DataFrame are displayed using `.head()` to inspect the data.
    * The structure of the dataset, including data types and non-null values, is explored using `.info()`.
    * The number of missing values in each column is checked using `.isnull().sum()`.
    * Basic handling of missing values (filling with the mean for demonstration, although the Iris dataset is typically clean) is included.

### Task 2: Basic Data Analysis

* **Objective:** To compute basic statistics and perform groupings to identify initial patterns in the data.
* **Implementation:**
    * Basic descriptive statistics (mean, median, standard deviation, etc.) for the numerical columns are computed using `.describe()`.
    * The dataset is grouped by the 'species' (target variable), and the mean of each numerical feature is calculated for each species using `.groupby()` and `.mean()`.
    * Observations and potential patterns based on the computed statistics and grouped means are identified and documented in the code output.

### Task 3: Data Visualization

* **Objective:** To create various types of visualizations to explore the data visually and identify relationships and distributions.
* **Implementation:**
    * The following four types of plots are generated using Matplotlib and Seaborn:
        1.  **Line Chart (adapted):** Showing the trend of average petal length across the Iris species (sorted by average petal length).
        2.  **Bar Chart:** Comparing the average petal length for each Iris species.
        3.  **Histogram:** Displaying the distribution of the 'sepal width (cm)' feature.
        4.  **Scatter Plot:** Visualizing the relationship between 'sepal length (cm)' and 'petal length (cm)', with points colored by species.
    * Each plot is customized with a clear title, labels for the x and y axes, and a legend where necessary to ensure interpretability. Seaborn styles are used to enhance the visual appeal of the plots.

## Error Handling

I did not use error handling because the Iris dataset comes directly from scikit-learn, which means:

- It's built in and well formatted.

-  No File I/O Involved.

- No Missing Values or Incorrect Data Types.

## How to Run the Code

1.  Ensure you have Python installed on your system.
2.  Install the necessary libraries:
    ```bash
    pip install pandas matplotlib seaborn scikit-learn
    ```
3.  Save the Python scripts 
4.  Run the script from your terminal:
    ```bash
    python iris_data_analysis.py
    ```
    The output will include the explored data, basic statistics, grouped means, and the generated plots will be displayed.

## Submission

This submission includes:
- iris_sklearn_load_explore_task1.py
- iris_data_analysis_task2.py
- iris_visualization_task3.py