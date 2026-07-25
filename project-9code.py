import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DEFAULT_CSV_PATH = "sales_data.csv"


def prepare_default_dataset(filepath=DEFAULT_CSV_PATH):
    """Automatically generates initial sample sales CSV if missing."""
    if not os.path.exists(filepath):
        records = {
            'SalesID': [101, 102, 103, 104, 105],
            'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
            'Region': ['North', 'East', 'West Coast', 'South', 'Central'],
            'Sales': [500, 600, 700, 800, 550],
            'Year': [2022, 2022, 2022, 2022, 2022]
        }
        pd.DataFrame(records).to_csv(filepath, index=False)
        print(f"[System Setup] Sample dataset created automatically at '{filepath}'.")


class DataManager:
    """Handles dataset operations, data cleaning, analysis, and plot generations."""

    def __init__(self, source_path=None):
        self.df = None
        self.active_figure = None
        if source_path:
            self.fetch_csv(source_path)

    def fetch_csv(self, path):
        if not os.path.exists(path):
            print(f"Error: File '{path}' not found.")
            return False
        try:
            self.df = pd.read_csv(path)
            print("Dataset loaded successfully!")
            return True
        except Exception as err:
            print(f"Error loading CSV file: {err}")
            return False

    def inspect_dataset(self, option_code):
        if self.df is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        match option_code:
            case 1:
                print("\n-- First 5 rows --")
                print(self.df.head())
            case 2:
                print("\n-- Last 5 rows --")
                print(self.df.tail())
            case 3:
                print("\n-- Column Names --")
                print(list(self.df.columns))
            case 4:
                print("\n-- Column Data Types --")
                print(self.df.dtypes)
            case 5:
                print("\n-- Basic Info --")
                print(self.df.info())
            case _:
                print("Invalid option.")

    def query_and_transform(self):
        if self.df is None:
            print("No dataset loaded.")
            return

        print("\n-- Search, Sort, & Filter --")
        print("1. Search by value in a column")
        print("2. Sort data by column")
        print("3. Filter data (e.g., numeric thresholds)")
        
        user_choice = input("Enter choice (1-3): ").strip()

        if user_choice == "1":
            target_col = input("Enter column name: ").strip()
            query_val = input("Enter value to search: ").strip()
            if target_col in self.df.columns:
                matches = self.df[self.df[target_col].astype(str).str.contains(query_val, case=False, na=False)]
                print(matches)
            else:
                print("Column not found.")

        elif user_choice == "2":
            target_col = input("Enter column to sort by: ").strip()
            direction = input("Sort ascending? (y/n): ").strip().lower() == 'y'
            if target_col in self.df.columns:
                sorted_view = self.df.sort_values(by=target_col, ascending=direction)
                print(sorted_view.head(10))
            else:
                print("Column not found.")

        elif user_choice == "3":
            num_col = input("Enter numeric column name to filter: ").strip()
            if num_col in self.df.columns and np.issubdtype(self.df[num_col].dtype, np.number):
                cutoff = float(input(f"Filter rows where {num_col} > : "))
                print(self.df[self.df[num_col] > cutoff])
            else:
                print("Invalid numeric column.")

    def generate_pivot(self, row_idx, val_col, aggregation='sum'):
        if self.df is None:
            print("No dataset loaded.")
            return
        
        try:
            pt = pd.pivot_table(self.df, values=val_col, index=row_idx, aggfunc=aggregation)
            print("\n-- Pivot Table --")
            print(pt)
        except Exception as err:
            print(f"Error creating pivot table: {err}")

    def missing_value_handler(self, mode):
        if self.df is None:
            print("No dataset loaded.")
            return

        total_missing = self.df.isnull().sum().sum()

        if mode == 1:
            if total_missing == 0:
                print("\nNo missing values found in the dataset!")
            else:
                print("\n-- Rows with missing values --")
                print(self.df[self.df.isnull().any(axis=1)])
        elif mode == 2:
            num_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
            print("Missing numerical values filled with mean.")
        elif mode == 3:
            self.df.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif mode == 4:
            custom_val = input("Enter replacement value: ").strip()
            self.df.fillna(custom_val, inplace=True)
            print(f"Missing values replaced with '{custom_val}'.")

    def run_stats(self):
        if self.df is None:
            print("No dataset loaded.")
            return

        print("\n-- Descriptive Statistics --")
        print(self.df.describe())
        
        numeric_data = self.df.select_dtypes(include=[np.number])
        if not numeric_data.empty:
            print("\nVariance:\n", numeric_data.var())
            print("\n25th & 75th Percentiles:\n", numeric_data.quantile([0.25, 0.75]))

    def render_plot(self, plot_kind):
        if self.df is None:
            print("No dataset loaded.")
            return

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.set_theme(style="whitegrid")

        try:
            if plot_kind == 1:
                x_axis = input("Enter x-axis column name: ").strip()
                y_axis = input("Enter y-axis column name: ").strip()
                sns.barplot(data=self.df, x=x_axis, y=y_axis, ax=ax)
                plt.title(f"Bar Plot: {y_axis} vs {x_axis}")

            elif plot_kind == 2:
                x_axis = input("Enter x-axis column name: ").strip()
                y_axis = input("Enter y-axis column name: ").strip()
                sns.lineplot(data=self.df, x=x_axis, y=y_axis, ax=ax)
                plt.title(f"Line Plot: {y_axis} vs {x_axis}")

            elif plot_kind == 3:
                x_axis = input("Enter x-axis column name: ").strip()
                y_axis = input("Enter y-axis column name: ").strip()
                print("Generating scatter plot...")
                sns.scatterplot(data=self.df, x=x_axis, y=y_axis, ax=ax)
                plt.title(f"Scatter Plot: {y_axis} vs {x_axis}")

            elif plot_kind == 4:
                target_col = input("Enter category column for Pie Chart: ").strip()
                counts = self.df[target_col].value_counts()
                ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
                plt.title(f"Pie Chart of {target_col}")

            elif plot_kind == 5:
                target_col = input("Enter numeric column name for Histogram: ").strip()
                sns.histplot(self.df[target_col], kde=True, ax=ax)
                plt.title(f"Histogram of {target_col}")

            elif plot_kind == 6:
                num_columns = self.df.select_dtypes(include=[np.number]).columns[:3]
                if len(num_columns) > 1:
                    ax.stackplot(range(len(self.df)), [self.df[col] for col in num_columns], labels=num_columns)
                    ax.legend(loc='upper left')
                    plt.title("Stack Plot")
                else:
                    print("Insufficient numeric columns for Stack Plot.")
                    plt.close(fig)
                    return
            else:
                print("Invalid plot choice.")
                plt.close(fig)
                return

            self.active_figure = fig
            plt.tight_layout()
            print("Plot generated successfully!")
            plt.show()

        except Exception as err:
            print(f"Error generating plot: {err}")
            plt.close(fig)

    def export_plot(self, save_path):
        if self.active_figure is None:
            print("No active plot available to save. Generate a plot first.")
            return
        try:
            self.active_figure.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Visualization saved as {save_path} successfully!")
        except Exception as err:
            print(f"Error saving visualization: {err}")


def main():
    prepare_default_dataset(DEFAULT_CSV_PATH)
    processor = DataManager()

    while True:
        print("\n" + "---------- Data Analysis & Visualization Program ----------")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("-" * 58)

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n-- Load Dataset --")
            filepath_input = input("Enter the path of the dataset (CSV file): ").strip()
            if not filepath_input:
                filepath_input = DEFAULT_CSV_PATH
            processor.fetch_csv(filepath_input)

        elif choice == "2":
            print("\n-- Explore Data --")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice.isdigit():
                processor.inspect_dataset(int(sub_choice))

        elif choice == "3":
            print("\n-- Perform DataFrame Operations --")
            print("1. Search, Sort, or Filter Data")
            print("2. Create Pivot Table")
            print("3. Convert DataFrame Column to NumPy Array")
            op_choice = input("Enter choice (1-3): ").strip()

            if op_choice == "1":
                processor.query_and_transform()
            elif op_choice == "2":
                idx_name = input("Enter index column: ").strip()
                val_name = input("Enter values column: ").strip()
                processor.generate_pivot(idx_name, val_name)
            elif op_choice == "3":
                col_name = input("Enter column name to convert: ").strip()
                if processor.df is not None and col_name in processor.df.columns:
                    array_data = processor.df[col_name].to_numpy()
                    print(f"NumPy Array: {array_data}")
                else:
                    print("Invalid column or dataset not loaded.")

        elif choice == "4":
            print("\n-- Handle Missing Data --")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            clean_choice = input("Enter your choice: ").strip()
            if clean_choice.isdigit():
                processor.missing_value_handler(int(clean_choice))

        elif choice == "5":
            print("\n-- Generate Descriptive Statistics --")
            processor.run_stats()

        elif choice == "6":
            print("\n-- Data Visualization --")
            print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart\n5. Histogram\n6. Stack Plot")
            viz_choice = input("Enter your choice: ").strip()
            if viz_choice.isdigit():
                processor.render_plot(int(viz_choice))

        elif choice == "7":
            print("\n-- Save Visualization --")
            file_out = input("Enter file name to save the plot (e.g., scatter_plot.png): ").strip()
            if file_out:
                processor.export_plot(file_out)

        elif choice == "8":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 8.")


if __name__ == "__main__":
    main()
