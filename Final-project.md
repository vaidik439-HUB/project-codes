
# Yahoo Stock Insider Trading Analysis & Exploration

## Project Overview

**Yahoo Stock Insider Trading Analysis & Exploration** is a Python-based data analysis and visualization project designed to explore insider trading transactions and financial activity using a stock market dataset.

The project uses **Pandas** and **NumPy** for data processing and statistical analysis, along with **Matplotlib** and **Seaborn** for creating meaningful visualizations.

The analysis focuses on transaction types, transaction values, reported prices, USD transaction volumes, and stock activity. It also includes data cleaning, descriptive statistics, financial metric calculations, transaction factor analysis, correlation analysis, and high-resolution plot exporting.

The main Python script is:

```text
insider_trading_analysis.py
````

The dataset used by the project is:

```text
yahooStock.csv
```

---

## Features

### 1. Dynamic Dataset Loading

* Loads the `yahooStock.csv` dataset dynamically using a custom file path.
* Automatically parses date-related columns where applicable.
* Provides flexibility for working with datasets stored in different locations.

### 2. Data Exploration

The project provides multiple options for understanding the structure and quality of the dataset:

* Displays the first few rows using `head()`.
* Displays the last few rows using `tail()`.
* Provides complete dataset information using `info()`.
* Counts missing values in each column.
* Calculates the number of unique values for every column.

### 3. Data Cleaning

The project handles missing and incomplete data using practical data-cleaning techniques:

* Missing `shortJobTitle` values are filled with:

```text
Not Specified
```

* Missing numerical values are imputed using the median of their respective columns.
* The cleaning process helps prepare the dataset for accurate analysis and visualization.

### 4. Descriptive Statistics

The project calculates descriptive statistics to summarize the dataset and understand transaction patterns.

The analysis includes:

* Count
* Mean
* Standard deviation
* Minimum value
* Maximum value
* Quartiles

These statistics help identify trends, distributions, and potential outliers within the financial data.

### 5. Key Financial Metrics

The project calculates important financial metrics, including:

* **Total USD Volume** - Total value of transactions measured in USD.
* **Average USD Value** - Average transaction value in USD.
* **Max Transaction Value** - Largest recorded transaction value.

These metrics provide a high-level overview of the financial activity represented in the dataset.

### 6. Transaction Factor Analysis

The project analyzes transaction activity based on the `transactionType` column.

The analysis includes:

* Grouping transactions by transaction type.
* Comparing **Buy** and **Sell** transactions.
* Calculating transaction-related financial metrics by transaction type.
* Identifying the **Top 5 Most Active Stocks** based on total USD volume.

This helps identify which stocks have the highest overall transaction activity.

### 7. Data Visualization

The project generates multiple visualizations to make financial patterns easier to understand.

Included visualizations:

* Transaction count plot by transaction type.
* Top 5 stocks by total USD volume.
* Reported price distribution histogram with KDE.
* Log-scale boxplot of transaction USD values by transaction type.
* Correlation heatmap for numerical features.

### 8. High-Resolution Plot Export

Generated visualizations can be exported directly as high-resolution PNG files.

This makes the charts suitable for:

* Reports
* Presentations
* Data analysis documentation
* Academic projects
* GitHub project documentation

---

## Technologies Used

The project is developed using the following technologies and libraries:

| Technology | Purpose                                              |
| ---------- | ---------------------------------------------------- |
| Python 3   | Core programming language                            |
| Pandas     | Data loading, cleaning, transformation, and analysis |
| NumPy      | Numerical calculations and statistical operations    |
| Matplotlib | Data visualization and plotting                      |
| Seaborn    | Statistical visualization and advanced charts        |

---

## Repository Structure

```text
Yahoo-Stock-Insider-Trading-Analysis/
│
├── insider_trading_analysis.py
├── yahooStock.csv
├── transaction_count_by_type.png
├── top_5_stocks_by_usd_volume.png
├── reported_price_distribution.png
├── transaction_usd_value_boxplot.png
├── numerical_correlation_heatmap.png
└── README.md
```

### File Description

| File                                | Description                                                            |
| ----------------------------------- | ---------------------------------------------------------------------- |
| `insider_trading_analysis.py`       | Main Python script containing the complete analysis workflow           |
| `yahooStock.csv`                    | Dataset containing Yahoo stock insider trading transaction records     |
| `transaction_count_by_type.png`     | Visualization comparing Buy and Sell transaction counts                |
| `top_5_stocks_by_usd_volume.png`    | Bar chart showing the top 5 most active stocks by total USD volume     |
| `reported_price_distribution.png`   | Histogram with KDE showing reported price distribution                 |
| `transaction_usd_value_boxplot.png` | Log-scale boxplot comparing transaction USD values by transaction type |
| `numerical_correlation_heatmap.png` | Correlation heatmap for numerical dataset features                     |
| `README.md`                         | Project documentation                                                  |

> **Note:** The PNG files are generated by the Python script when the visualization and export functionality is executed.

---

## Installation & Requirements

### Prerequisites

Make sure the following software is installed on your system:

* Python 3.x
* pip
* Git (optional, for cloning the repository)

### Required Python Libraries

Install the required dependencies using:

```bash
pip install pandas numpy matplotlib seaborn
```

Alternatively, install all dependencies together:

```bash
pip install pandas numpy matplotlib seaborn
```

### Verify Python Installation

Check your Python version using:

```bash
python --version
```

or:

```bash
python3 --version
```

### Verify pip Installation

```bash
pip --version
```

---

## How to Run

### Step 1: Clone the Repository

Clone the project repository using Git:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Yahoo-Stock-Insider-Trading-Analysis
```

### Step 2: Install Dependencies

Install all required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 3: Verify the Dataset

Make sure the dataset is available at the expected location:

```text
yahooStock.csv
```

If the script accepts a custom file path, provide the correct path to the dataset when prompted or configured.

### Step 4: Run the Analysis

Run the main Python script:

```bash
python insider_trading_analysis.py
```

On systems where Python 3 is accessed using `python3`, run:

```bash
python3 insider_trading_analysis.py
```

### Step 5: Review the Results

The script performs data exploration, cleaning, statistical analysis, financial metric calculations, transaction factor analysis, and visualization.

Generated high-resolution PNG files can be viewed in the project directory.

---

## Analysis Workflow

The project follows a structured data analysis workflow:

```text
Load Dataset
     │
     ▼
Parse Dates
     │
     ▼
Explore Dataset
     │
     ├── Head / Tail
     ├── Dataset Information
     ├── Missing Values
     └── Unique Values
     │
     ▼
Clean Data
     │
     ├── Fill Missing Job Titles
     └── Impute Numerical Missing Values
     │
     ▼
Descriptive Statistics
     │
     ▼
Calculate Financial Metrics
     │
     ├── Total USD Volume
     ├── Average USD Value
     └── Maximum Transaction Value
     │
     ▼
Transaction Factor Analysis
     │
     ├── Buy vs Sell Analysis
     └── Top 5 Active Stocks
     │
     ▼
Generate Visualizations
     │
     ├── Transaction Count Plot
     ├── Top 5 Stock Volume Chart
     ├── Reported Price Histogram
     ├── Transaction Value Boxplot
     └── Correlation Heatmap
     │
     ▼
Export High-Resolution PNG Files
```

---

## Visualizations Included

### 1. Transaction Count by Type

This plot compares the number of transactions for different transaction types.

The primary comparison is between:

* **Buy**
* **Sell**

This visualization helps identify whether buying or selling transactions are more frequent in the dataset.

---

### 2. Top 5 Stocks by Total USD Volume

A bar chart is generated to identify the five most active stocks based on their total USD transaction volume.

This visualization helps highlight stocks with the highest financial transaction activity.

---

### 3. Reported Price Distribution

A histogram with KDE is used to visualize the distribution of reported stock transaction prices.

It helps analyze:

* Price concentration
* Distribution shape
* Possible skewness
* Potential unusual values

---

### 4. Transaction USD Value by Transaction Type

A log-scale boxplot is used to compare transaction USD values across transaction types.

The logarithmic scale is useful when transaction values vary significantly in magnitude.

The visualization helps identify:

* Median transaction values
* Distribution ranges
* Potential outliers
* Differences between transaction types

---

### 5. Numerical Features Correlation Heatmap

A Seaborn correlation heatmap is generated for numerical features in the dataset.

The heatmap helps identify relationships between numerical variables and provides insight into:

* Positive correlations
* Negative correlations
* Weak relationships
* Strong relationships

---

## Data Cleaning Methodology

The project uses the following data-cleaning approach:

### Missing Categorical Values

Missing values in the `shortJobTitle` column are replaced with:

```python
"Not Specified"
```

This ensures that missing job-title information is represented consistently without removing the associated transaction records.

### Missing Numerical Values

Missing numerical values are replaced using the median value of their respective columns.

Median imputation is useful because it is less affected by extreme values and outliers than mean-based imputation.

---

## Key Metrics

The project calculates the following financial metrics:

### Total USD Volume

Represents the combined USD value of relevant stock transactions.

### Average USD Value

Represents the average transaction value in USD.

### Maximum Transaction Value

Identifies the highest transaction value recorded in the dataset.

These metrics provide a concise summary of the financial scale of the insider trading activity being analyzed.

---

## Transaction Analysis

The project groups transaction records according to:

```text
transactionType
```

This allows the analysis to compare different transaction categories, particularly:

```text
Buy
Sell
```

The project also identifies the top five stocks with the highest total USD transaction volume.

This analysis can help users explore patterns in stock activity and transaction behavior within the dataset.

---

## Output Files

After successful execution, the project can generate high-resolution PNG visualization files such as:

```text
transaction_count_by_type.png
top_5_stocks_by_usd_volume.png
reported_price_distribution.png
transaction_usd_value_boxplot.png
numerical_correlation_heatmap.png
```

These files can be used independently in reports, presentations, or project documentation.

---

## Example Commands

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Run the Script

```bash
python insider_trading_analysis.py
```

### Run with Python 3

```bash
python3 insider_trading_analysis.py
```

---

## Use Cases

This project can be useful for:

* Learning Python-based data analysis.
* Practicing Pandas data manipulation.
* Understanding financial transaction datasets.
* Exploring insider trading data.
* Learning data cleaning techniques.
* Performing descriptive statistical analysis.
* Creating financial data visualizations.
* Practicing exploratory data analysis (EDA).
* Building a portfolio project for data analytics.
* Understanding transaction-level stock market data.

---

## Important Note

This project is intended for **educational and analytical purposes only**.

The analysis and visualizations generated by this project should not be considered financial advice, investment recommendations, or predictions of future stock performance.

The results depend entirely on the quality, completeness, and accuracy of the provided `yahooStock.csv` dataset.

---

## Future Improvements

Potential improvements for future versions include:

* Adding interactive dashboards using Streamlit or Plotly.
* Adding automated data validation.
* Supporting multiple input datasets.
* Adding more advanced statistical analysis.
* Adding time-series analysis of insider transactions.
* Analyzing insider transaction trends over time.
* Adding stock-level transaction comparisons.
* Including automated HTML or PDF report generation.
* Adding unit tests for data-processing functions.
* Adding a `requirements.txt` file for dependency management.
* Adding command-line arguments for dataset paths and output directories.
* Implementing structured logging and error handling.
* Adding automated data-quality reports.

---

## Requirements File

For easier dependency installation, a `requirements.txt` file can contain:

```text
pandas
numpy
matplotlib
seaborn
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Project Goals

The primary goals of this project are to:

1. Load and explore a real-world-style stock transaction dataset.
2. Clean missing and incomplete data.
3. Calculate meaningful financial statistics.
4. Analyze transaction activity by transaction type.
5. Identify the most active stocks based on transaction volume.
6. Visualize financial and transaction patterns.
7. Export high-quality visualizations for further use.
8. Demonstrate practical Python data analysis skills.

---

## License

This project is provided for **educational and learning purposes**.

You are free to use, modify, and extend the project for personal learning and development.

If you distribute or significantly modify the project, consider adding an appropriate open-source license such as the **MIT License**.

---

This project was created as a practical Python data analysis and exploratory data visualization project using:

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
```

---

## Conclusion

**Yahoo Stock Insider Trading Analysis & Exploration** demonstrates a complete exploratory data analysis workflow for stock insider trading data.

The project combines:

* Data loading
* Date parsing
* Data exploration
* Missing-value handling
* Data cleaning
* Descriptive statistics
* Financial metric calculations
* Transaction factor analysis
* Stock activity analysis
* Data visualization
* Correlation analysis
* High-resolution plot exporting

It provides a practical foundation for understanding how Python and popular data science libraries can be used to analyze financial datasets and discover meaningful patterns in transaction activity.

```
