
# COVID-19 Country & Regional Data Analysis System 🌍

> **An interactive Python CLI application for exploring, cleaning, analyzing, and visualizing global COVID-19 country and regional data.**

---

## Project Overview

The **COVID-19 Country & Regional Data Analysis System** is an interactive **Python Command-Line Interface (CLI)** application designed to perform comprehensive data analysis on a global COVID-19 dataset.

The project uses a dataset containing COVID-19 statistics from **187 countries and regions** and provides tools for:

-  Dynamic CSV dataset loading
-  Dataset exploration
-  Automated data cleaning
-  Feature engineering
-  Descriptive statistical analysis
-  Global COVID-19 totals
-  WHO regional analysis
-  Identification of highly affected countries
-  Data visualization
-  Exporting charts as image files

The application is designed to demonstrate practical data analysis techniques using popular Python data science libraries such as **Pandas, NumPy, Matplotlib, and Seaborn**.

---

## Project Goals

The primary goals of this project are to:

- Understand the structure and quality of real-world COVID-19 data.
- Explore country-level and regional COVID-19 statistics.
- Clean and preprocess raw datasets for reliable analysis.
- Calculate additional analytical metrics through feature engineering.
- Identify countries and regions most affected by COVID-19.
- Analyze relationships between different COVID-19 indicators.
- Present analytical findings through clear and meaningful visualizations.
- Provide an interactive CLI-based data analysis experience.

---

# Dataset Information

The project uses the following dataset:

```text
country_wise_latest.csv
````

The dataset contains COVID-19 statistics for **187 countries and regions** across **15 columns**.

The dataset includes information about:

* Confirmed COVID-19 cases
* Deaths
* Recovered cases
* Active cases
* New daily cases
* New deaths
* New recoveries
* Mortality rates
* Recovery rates
* Weekly changes
* WHO regional classification

---

# Dataset Column Schema

| Column Name              | Description                                                   |
| ------------------------ | ------------------------------------------------------------- |
| `Country/Region`         | Name of the country or region                                 |
| `Confirmed`              | Total number of confirmed COVID-19 cases                      |
| `Deaths`                 | Total number of reported COVID-19 deaths                      |
| `Recovered`              | Total number of recovered COVID-19 cases                      |
| `Active`                 | Number of currently active COVID-19 cases                     |
| `New cases`              | Newly reported COVID-19 cases                                 |
| `New deaths`             | Newly reported COVID-19 deaths                                |
| `New recovered`          | Newly reported recovered cases                                |
| `Deaths / 100 Cases`     | Deaths expressed as a percentage of confirmed cases           |
| `Recovered / 100 Cases`  | Recovered cases expressed as a percentage of confirmed cases  |
| `Deaths / 100 Recovered` | Deaths relative to recovered cases                            |
| `Confirmed last week`    | Total confirmed cases reported in the previous week           |
| `1 week change`          | Change in confirmed cases over one week                       |
| `1 week % increase`      | Percentage increase in confirmed cases over one week          |
| `WHO Region`             | WHO geographical region associated with the country or region |

---

# Core Features & Capabilities

## 1. Dynamic Dataset Loading & Exploration

The application supports dynamic loading of the COVID-19 CSV dataset.

Users can explore the structure and contents of the dataset through the CLI.

### Dataset Exploration Includes:

* View the first rows using `head()`
* View the last rows using `tail()`
* Inspect dataset shape
* Display column names
* Review data types
* Check dataset information
* Identify missing/null values
* Count unique values
* Explore numerical columns

This provides a quick understanding of the dataset before performing further analysis.

---

## 2. Data Cleaning & Automated Handling

Real-world datasets may contain missing values, invalid calculations, and infinite values.

The application automatically performs data-cleaning operations to improve analysis reliability.

### Cleaning Operations Include:

* Detection of missing values
* Handling of null entries
* Identification of infinite values
* Replacement of division-by-zero infinite values
* Median-based replacement for invalid infinite values

For example, metrics such as:

```text
Deaths / 100 Recovered
```

may generate infinite values when the number of recovered cases is zero.

The application replaces these invalid infinite values with appropriate **median values** to maintain numerical consistency during analysis.

---

## 3. Feature Engineering

The application creates additional analytical metrics from existing dataset columns.

One of the key engineered features is:

```text
Active / 100 Cases
```

This metric represents the proportion of active cases relative to total confirmed cases.

Feature engineering helps provide additional insights that may not be directly available in the original dataset.

---

## 4. Descriptive Statistics

The application provides statistical summaries of numerical COVID-19 data.

Users can analyze statistics such as:

* Count
* Mean
* Standard deviation
* Minimum
* 25th percentile
* Median
* 75th percentile
* Maximum

The analysis can be applied to important numerical variables including:

```text
Confirmed
Deaths
Recovered
Active
New cases
New deaths
New recovered
Deaths / 100 Cases
Recovered / 100 Cases
1 week change
1 week % increase
```

This helps users understand the overall distribution and variation of COVID-19 statistics.

---

## 5. Global COVID-19 Totals

The application calculates and displays global aggregate values for major COVID-19 indicators.

### Global Metrics Include:

*  Total Confirmed Cases
*  Total Deaths
*  Total Recovered Cases
*  Total Active Cases

These totals provide a high-level overview of the global impact represented by the dataset.

---

## 6. WHO Regional Analysis

The application aggregates COVID-19 statistics according to the **WHO Region** classification.

Regional analysis allows users to compare the impact of COVID-19 across different geographical areas.

### Regional Analysis Includes:

* Total confirmed cases by WHO Region
* Total deaths by WHO Region
* Total recovered cases by WHO Region
* Total active cases by WHO Region
* Regional comparison of COVID-19 impact

This helps identify which WHO regions experienced the highest overall case burden.

---

## 7. Top Affected Countries

The application identifies countries with the highest COVID-19 impact based on important metrics.

### Country-Level Rankings Include:

*  Top countries by confirmed cases
*  Top countries by death toll
*  Countries with significant case increases
*  Comparison of COVID-19 impact across countries

These rankings make it easier to identify countries that experienced particularly high numbers of cases or deaths.

---

## 8. Data Visualization

The project uses **Matplotlib** and **Seaborn** to generate clear and informative visualizations.

The visualizations help transform numerical COVID-19 data into easily understandable graphical insights.

The application includes multiple charts covering:

* Country-level comparisons
* Regional comparisons
* Death statistics
* Mortality distributions
* Correlations between numerical variables

---

## 9. Chart Export Functionality

The application provides an option to save generated visualizations as image files.

Supported formats include:

```text
.png
.jpg
```

This allows users to save charts for:

* Reports
* Presentations
* Research
* Documentation
* Data analysis portfolios
* Further use outside the application

---

# Visualizations Included

The project generates the following visualizations:

---

## 1. Top 10 Countries by Confirmed Cases

A bar chart displaying the **10 countries with the highest number of confirmed COVID-19 cases**.

This visualization provides a quick comparison of the countries most affected by total confirmed infections.

---

## 2. WHO Regional Case Totals

A regional comparison chart showing the total confirmed COVID-19 cases aggregated by **WHO Region**.

This visualization helps identify differences in the overall COVID-19 burden across WHO geographical regions.

---

## 3. Top 10 Countries by Deaths

A bar chart showing the **10 countries with the highest reported COVID-19 death counts**.

This provides a direct comparison of the countries with the largest reported death tolls.

---

## 4. Mortality Rate Distribution Histogram

A histogram showing the distribution of:

```text
Deaths / 100 Cases
```

This visualization helps analyze how COVID-19 mortality rates vary across the countries and regions included in the dataset.

---

## 5. Correlation Heatmap

A Seaborn correlation heatmap displaying relationships between numerical COVID-19 variables.

The heatmap can help identify relationships between metrics such as:

* Confirmed cases
* Deaths
* Recovered cases
* Active cases
* New cases
* Weekly changes
* Percentage increases
* Mortality rates
* Recovery rates

This is useful for identifying strong positive or negative correlations within the dataset.

---

# Repository Directory Structure

```text
COVID-19-Country-Regional-Data-Analysis/
│
├── covid_data_analysis.py
├── country_wise_latest.csv
├── README.md
│
└── visualizations/
    ├── top_10_confirmed_cases.png
    ├── who_regional_case_totals.png
    ├── top_10_deaths.png
    ├── mortality_rate_distribution.png
    └── correlation_heatmap.png
```

> **Note:** The `visualizations/` directory is optional and may be created when exported charts are saved by the application.

---

# Installation & Prerequisites

## Python Requirement

Make sure **Python 3.x** is installed on your system.

You can check your Python version using:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Required Python Libraries

The project requires the following Python libraries:

* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**

Install all dependencies using:

```bash
pip install numpy pandas matplotlib seaborn
```

Alternatively, install them individually:

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
```

---

# How to Run the Project

Follow the steps below to run the COVID-19 Data Analysis System.

---

## Step 1: Clone the Repository

Clone the GitHub repository using:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd COVID-19-Country-Regional-Data-Analysis
```

---

## Step 2: Verify the Dataset

Make sure the dataset file is available in the project directory:

```text
country_wise_latest.csv
```

The expected project structure should look like:

```text
COVID-19-Country-Regional-Data-Analysis/
│
├── covid_data_analysis.py
├── country_wise_latest.csv
└── README.md
```

---

## Step 3: Install Dependencies

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn
```

---

## Step 4: Run the Application

Execute the main Python script:

```bash
python covid_data_analysis.py
```

On systems where Python 3 is accessed using `python3`, run:

```bash
python3 covid_data_analysis.py
```

---

## Step 5: Use the Interactive CLI

After launching the program, follow the instructions displayed in the terminal.

The interactive CLI allows users to access different analysis operations such as:

* Dataset exploration
* Data cleaning
* Statistical summaries
* Global totals
* Regional analysis
* Top affected countries
* Data visualizations
* Chart export

Select the required option from the CLI menu and follow the prompts.

---

# Example Analysis Workflow

A typical analysis workflow can be summarized as:

```text
Load Dataset
      │
      ▼
Explore Dataset
      │
      ▼
Check Missing & Invalid Values
      │
      ▼
Clean Data
      │
      ▼
Perform Feature Engineering
      │
      ▼
Generate Descriptive Statistics
      │
      ▼
Calculate Global Totals
      │
      ▼
Perform Regional Analysis
      │
      ▼
Identify Top Affected Countries
      │
      ▼
Generate Visualizations
      │
      ▼
Export Charts
```

---

# Technologies Used

| Technology     | Purpose                                              |
| -------------- | ---------------------------------------------------- |
| **Python 3.x** | Core programming language                            |
| **Pandas**     | Data loading, cleaning, transformation, and analysis |
| **NumPy**      | Numerical operations and statistical calculations    |
| **Matplotlib** | Data visualization and chart generation              |
| **Seaborn**    | Statistical visualization and correlation heatmaps   |
| **CSV**        | Source dataset format                                |

---

# Key Learning Outcomes

This project demonstrates practical knowledge of:

* Python programming
* Command-Line Interface development
* Pandas DataFrames
* CSV data processing
* Data cleaning and preprocessing
* Missing-value handling
* Infinite-value handling
* Median-based data replacement
* Feature engineering
* Descriptive statistics
* Data aggregation
* GroupBy operations
* Regional data analysis
* Ranking and sorting
* Data visualization
* Matplotlib chart creation
* Seaborn statistical visualization
* Correlation analysis
* Chart exporting

---

# Example Use Cases

This project can be used for:

*  Academic data analysis projects
*  Data science learning
*  Python portfolio development
*  Exploratory Data Analysis (EDA)
*  COVID-19 statistical exploration
*  Learning Pandas and NumPy
*  Learning data visualization
*  Demonstrating data analysis skills on GitHub

---

#  Important Note

The analysis and visualizations generated by this project are based entirely on the data available in:

```text
country_wise_latest.csv
```

The dataset represents a specific snapshot of COVID-19 statistics and should not be interpreted as a source of current or real-time COVID-19 information.

For current public health information, always refer to official health organizations and government sources.

---

#  License

This project is licensed under the **MIT License**.

You are free to:

* Use the project
* Copy the project
* Modify the source code
* Distribute the project
* Use the project for personal or commercial purposes

A copy of the MIT License can be included in the repository as:

```text
LICENSE
```

---

#  Author

**Mihir Parmar**

If you found this project useful, consider giving the repository a  on GitHub!

---

## Project Summary

> **COVID-19 Country & Regional Data Analysis System** is a Python-based interactive CLI data analysis application that combines **data exploration, cleaning, feature engineering, statistical analysis, regional comparisons, country rankings, and professional visualizations** to explore global COVID-19 data from 187 countries and regions.

```
```
