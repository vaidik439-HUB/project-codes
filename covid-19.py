import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class CovidDataAnalyzer:

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
            print(f"\nCOVID-19 dataset successfully loaded from '{file_path}'!")
            print(f"Total Countries/Records: {self.data.shape[0]} | Total Columns: {self.data.shape[1]}")
            return True
        except Exception as e:
            print(f"\nError loading CSV file: {e}")
            return False

    def explore_data(self, option):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        if option == 1:
            print("\n-- First 5 Rows --")
            print(self.data.head())
        elif option == 2:
            print("\n-- Last 5 Rows --")
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

        print("\nCleaning COVID-19 dataset...")

        # Handle Infinite values (e.g., division by zero in 'Deaths / 100 Recovered')
        num_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[num_cols] = self.data[num_cols].replace([np.inf, -np.inf], np.nan)

        for col in num_cols:
            if self.data[col].isnull().sum() > 0:
                median_val = self.data[col].median()
                self.data[col].fillna(median_val, inplace=True)
                print(f"* Handled missing/infinite values in '{col}' (replaced with median: {median_val:.2f}).")

        cat_cols = self.data.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if self.data[col].isnull().sum() > 0:
                mode_val = self.data[col].mode()[0]
                self.data[col].fillna(mode_val, inplace=True)
                print(f"* Filled missing categorical values in '{col}' with '{mode_val}'.")

        # Feature Engineering: Active Case Rate
        if {'Active', 'Confirmed'}.issubset(self.data.columns):
            self.data['Active / 100 Cases'] = np.where(
                self.data['Confirmed'] > 0,
                (self.data['Active'] / self.data['Confirmed']) * 100,
                0
            )
            print("* Calculated 'Active / 100 Cases' feature.")

        print("Data cleaning completed successfully!")

    def statistical_summary(self):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        print("\n-- Descriptive Statistics (COVID-19 Metrics) --")
        print(self.data.describe())

        if 'Confirmed' in self.data.columns:
            total_cases = self.data['Confirmed'].sum()
            total_deaths = self.data['Deaths'].sum() if 'Deaths' in self.data.columns else 0
            total_recovered = self.data['Recovered'].sum() if 'Recovered' in self.data.columns else 0
            total_active = self.data['Active'].sum() if 'Active' in self.data.columns else 0

            print("\n-- Global COVID-19 Totals --")
            print(f"Total Confirmed Cases: {total_cases:,.0f}")
            print(f"Total Deaths:          {total_deaths:,.0f}")
            print(f"Total Recovered:       {total_recovered:,.0f}")
            print(f"Total Active Cases:    {total_active:,.0f}")

    def analyze_factors(self):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        print("\n" + "=" * 45)
        print("    COVID-19 REGIONAL & COUNTRY ANALYSIS   ")
        print("=" * 45)

        country_col = 'Country/Region' if 'Country/Region' in self.data.columns else 'Country'

        if country_col in self.data.columns and 'Confirmed' in self.data.columns:
            print("\n-- Top 5 Countries by Confirmed Cases --")
            top_confirmed = self.data.groupby(country_col)['Confirmed'].sum().nlargest(5)
            print(top_confirmed)

            if 'Deaths' in self.data.columns:
                print("\n-- Top 5 Countries by Total Deaths --")
                top_deaths = self.data.groupby(country_col)['Deaths'].sum().nlargest(5)
                print(top_deaths)

        if 'WHO Region' in self.data.columns:
            print("\n-- Total Cases by WHO Region --")
            region_summary = self.data.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum()
            print(region_summary)

    def visualize_data(self, plot_type):
        if self.data is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.set_theme(style="whitegrid")

        country_col = 'Country/Region' if 'Country/Region' in self.data.columns else 'Country'

        try:
            if plot_type == 1:
                if country_col in self.data.columns and 'Confirmed' in self.data.columns:
                    top10 = self.data.groupby(country_col)['Confirmed'].sum().nlargest(10).reset_index()
                    sns.barplot(data=top10, x='Confirmed', y=country_col, palette='Reds_r', ax=ax)
                    plt.title("Top 10 Countries by Confirmed Cases")
                    plt.xlabel("Total Confirmed Cases")

            elif plot_type == 2:
                if 'WHO Region' in self.data.columns and 'Confirmed' in self.data.columns:
                    region_data = self.data.groupby('WHO Region')['Confirmed'].sum().reset_index()
                    sns.barplot(data=region_data, x='WHO Region', y='Confirmed', palette='Set2', ax=ax)
                    plt.title("Total Confirmed Cases by WHO Region")
                    plt.xticks(rotation=30)
                    plt.ylabel("Confirmed Cases")

            elif plot_type == 3:
                if country_col in self.data.columns and 'Deaths' in self.data.columns:
                    top10_deaths = self.data.groupby(country_col)['Deaths'].sum().nlargest(10).reset_index()
                    sns.barplot(data=top10_deaths, x='Deaths', y=country_col, palette='Dark2', ax=ax)
                    plt.title("Top 10 Countries by Total Deaths")
                    plt.xlabel("Total Deaths")

            elif plot_type == 4:
                if 'Deaths / 100 Cases' in self.data.columns:
                    sns.histplot(self.data['Deaths / 100 Cases'], kde=True, color='purple', bins=20, ax=ax)
                    plt.title("Distribution of Mortality Rate (Deaths / 100 Cases)")
                    plt.xlabel("Deaths / 100 Cases")

            elif plot_type == 5:
                num_df = self.data.select_dtypes(include=[np.number])
                sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
                plt.title("Correlation Heatmap Across COVID-19 Metrics")

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
    analyzer = CovidDataAnalyzer()

    while True:
        print("\n" + "=" * 12 + " COVID-19 Country & Region Analysis " + "=" * 12)
        print("1. Load CSV File Path")
        print("2. Explore Data (Head, Tail, Info, Missing Values)")
        print("3. Clean Dataset & Handle Infinite Values")
        print("4. Display Statistics & Global Totals")
        print("5. Analyze Regional (WHO) & Top Country Breakdown")
        print("6. Generate Visualizations & Charts")
        print("7. Save Active Plot to Image File")
        print("8. Exit")
        print("=" * 60)

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            path = input("Enter CSV path (default: country_wise_latest.csv): ").strip()
            if not path:
                path = "country_wise_latest.csv"
            analyzer.load_data(path)

        elif choice == "2":
            print("\n-- Exploration Options --")
            print("1. First 5 Rows")
            print("2. Last 5 Rows")
            print("3. Summary Info")
            print("4. Missing Values Count")
            print("5. Unique Value Counts")
            sub_choice = input("Choice: ").strip()
            if sub_choice.isdigit():
                analyzer.explore_data(int(sub_choice))

        elif choice == "3":
            analyzer.clean_data()

        elif choice == "4":
            analyzer.statistical_summary()

        elif choice == "5":
            analyzer.analyze_factors()

        elif choice == "6":
            print("\n-- Visualization Options --")
            print("1. Top 10 Countries by Confirmed Cases")
            print("2. Total Confirmed Cases by WHO Region")
            print("3. Top 10 Countries by Total Deaths")
            print("4. Distribution of Mortality Rate (Deaths / 100 Cases)")
            print("5. Correlation Heatmap Across Metrics")
            v_choice = input("Choice: ").strip()
            if v_choice.isdigit():
                analyzer.visualize_data(int(v_choice))

        elif choice == "7":
            filename = input("Enter filename to save plot (e.g., covid_chart.png): ").strip()
            if filename:
                analyzer.save_visualization(filename)

        elif choice == "8":
            print("\nExiting COVID-19 Analysis System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
