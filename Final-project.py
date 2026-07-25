import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class YahooStockAnalyzer:

    def __init__(self, file_path=None):
        self.data = None
        self.last_fig = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        plt.close("all")

    def load_data(self, file_path):
        if not os.path.exists(file_path):
            print(f"\nError: File '{file_path}' not found. Please check the path and try again.")
            return False
        try:
            self.data = pd.read_csv(file_path)
            if 'transactionDate' in self.data.columns:
                self.data['transactionDate'] = pd.to_datetime(self.data['transactionDate'])
            print(f"\nYahoo stock dataset successfully loaded from '{file_path}'!")
            print(f"Total Transactions: {self.data.shape[0]} | Total Columns: {self.data.shape[1]}")
            return True
        except Exception as e:
            print(f"\nError loading CSV file: {e}")
            return False

    def explore_data(self, option):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        if option == 1:
            print("\n-- First 5 Transactions --")
            print(self.data.head())
        elif option == 2:
            print("\n-- Last 5 Transactions --")
            print(self.data.tail())
        elif option == 3:
            print("\n-- Dataset Summary Info --")
            print(self.data.info())
        elif option == 4:
            print("\n-- Missing Values Count --")
            print(self.data.isnull().sum())
        elif option == 5:
            print("\n-- Unique Counts per Column --")
            print(self.data.nunique())
        else:
            print("\nInvalid choice.")

    def clean_data(self):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        print("\nCleaning missing transaction data...")

        if 'shortJobTitle' in self.data.columns and self.data['shortJobTitle'].isnull().sum() > 0:
            self.data['shortJobTitle'].fillna('Not Specified', inplace=True)
            print("* Filled missing 'shortJobTitle' values with 'Not Specified'.")

        num_cols = self.data.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if self.data[col].isnull().sum() > 0:
                median_val = self.data[col].median()
                self.data[col].fillna(median_val, inplace=True)
                print(f"* Filled missing values in '{col}' with median ({median_val}).")

        print("Data cleaning completed successfully!")

    def statistical_summary(self):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        print("\n-- Descriptive Statistics (Numerical Fields) --")
        print(self.data.describe())

        if 'usdValue' in self.data.columns:
            total_val = self.data['usdValue'].sum()
            avg_val = self.data['usdValue'].mean()
            max_val = self.data['usdValue'].max()
            print("\n-- Key Financial Metrics --")
            print(f"Total Transaction Value: ${total_val:,.2f}")
            print(f"Average Transaction Value: ${avg_val:,.2f}")
            print(f"Largest Transaction Value: ${max_val:,.2f}")

    def analyze_transaction_factors(self):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        print("\n" + "=" * 40)
        print("        TRANSACTION FACTOR ANALYSIS        ")
        print("=" * 40)

        if 'transactionType' in self.data.columns:
            print("\n-- Transactions by Type --")
            tt_summary = self.data.groupby('transactionType').agg(
                Count=('usdValue', 'count'),
                Total_USD_Value=('usdValue', 'sum'),
                Avg_USD_Value=('usdValue', 'mean')
            )
            print(tt_summary)

        if 'symbol' in self.data.columns and 'usdValue' in self.data.columns:
            print("\n-- Top 5 Most Active Stocks by USD Volume --")
            top_stocks = self.data.groupby('symbol')['usdValue'].sum().nlargest(5)
            print(top_stocks)

    def visualize_data(self, plot_type):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.set_theme(style="whitegrid")

        try:
            if plot_type == 1:
                if 'transactionType' in self.data.columns:
                    sns.countplot(data=self.data, x='transactionType', palette='Set2', ax=ax)
                    plt.title("Transaction Count by Type (Buy vs Sell)")
                    plt.xlabel("Transaction Type")
                    plt.ylabel("Count")

            elif plot_type == 2:
                if 'symbol' in self.data.columns and 'usdValue' in self.data.columns:
                    top5 = self.data.groupby('symbol')['usdValue'].sum().nlargest(5).reset_index()
                    sns.barplot(data=top5, x='symbol', y='usdValue', palette='Blues_r', ax=ax)
                    plt.title("Top 5 Stocks by Total USD Transaction Volume")
                    plt.xlabel("Stock Symbol")
                    plt.ylabel("Total Value ($)")

            elif plot_type == 3:
                if 'reportedPrice' in self.data.columns:
                    sns.histplot(self.data['reportedPrice'], kde=True, bins=30, color='teal', ax=ax)
                    plt.title("Reported Price Distribution")
                    plt.xlabel("Reported Price ($)")

            elif plot_type == 4:
                if 'transactionType' in self.data.columns and 'usdValue' in self.data.columns:
                    sns.boxplot(data=self.data, x='transactionType', y='usdValue', palette='Set3', ax=ax)
                    ax.set_yscale('log')
                    plt.title("Transaction USD Value by Type (Log Scale)")
                    plt.xlabel("Transaction Type")
                    plt.ylabel("USD Value (Log Scale)")

            elif plot_type == 5:
                num_df = self.data.select_dtypes(include=[np.number])
                sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
                plt.title("Correlation Heatmap")

            else:
                print("Invalid plot choice.")
                plt.close(fig)
                return

            self.last_fig = fig
            plt.tight_layout()
            print("Plot generated successfully!")
            plt.show()

        except Exception as e:
            print(f"Error generating plot: {e}")
            plt.close(fig)

    def save_visualization(self, filename):
        if self.last_fig is None:
            print("\nNo active plot to save. Generate a plot first.")
            return
        try:
            self.last_fig.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"\nSaved plot successfully as '{filename}'.")
        except Exception as e:
            print(f"\nError saving image: {e}")


def main():
    analyzer = YahooStockAnalyzer()

    while True:
        print("\n" + "=" * 12 + " Yahoo Stock Insider Trading System " + "=" * 12)
        print("1. Load CSV File Path")
        print("2. Explore Data (Head, Info, Missing Values)")
        print("3. Clean Dataset (Handle Missing Job Titles & Values)")
        print("4. Display Descriptive Statistics")
        print("5. Analyze Transaction Breakdown (Buy/Sell & Top Stocks)")
        print("6. Generate Visualizations & Charts")
        print("7. Save Active Plot to Image File")
        print("8. Exit")
        print("=" * 60)

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            path = input("Enter path to CSV (e.g., yahooStock.csv): ").strip()
            if path:
                analyzer.load_data(path)
            else:
                print("Path cannot be empty.")

        elif choice == "2":
            print("\n-- Exploration Options --")
            print("1. First 5 Rows")
            print("2. Last 5 Rows")
            print("3. Dataset Summary Info")
            print("4. Missing Values Count")
            print("5. Unique Values Count")
            sub_choice = input("Choice: ").strip()
            if sub_choice.isdigit():
                analyzer.explore_data(int(sub_choice))

        elif choice == "3":
            analyzer.clean_data()

        elif choice == "4":
            analyzer.statistical_summary()

        elif choice == "5":
            analyzer.analyze_transaction_factors()

        elif choice == "6":
            print("\n-- Visualization Options --")
            print("1. Transaction Count by Type (Buy/Sell)")
            print("2. Top 5 Stocks by USD Volume")
            print("3. Reported Price Distribution")
            print("4. Transaction Value Boxplot by Type")
            print("5. Correlation Heatmap")
            v_choice = input("Choice: ").strip()
            if v_choice.isdigit():
                analyzer.visualize_data(int(v_choice))

        elif choice == "7":
            filename = input("Enter filename to save plot (e.g., transaction_chart.png): ").strip()
            if filename:
                analyzer.save_visualization(filename)

        elif choice == "8":
            print("\nExiting Yahoo Stock Analysis Program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
