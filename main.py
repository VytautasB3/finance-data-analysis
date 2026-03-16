print("Starting data analysis")

#importing path command from pathlib
from pathlib import Path

# Importing pandas for easy data manipulation
import pandas as pd

# Importing bar chart tools from openpyxl
from openpyxl.chart import BarChart, Reference

# Importing function from data_analysis
from data_analysis import (
    load_data,
    total_revenue_all_time,
    total_revenue_between_years,
    total_revenue_for_year,
    average_interest_last_n_years,
)


# Helper function to convert Series or DataFrame into a chart-friendly DataFrame
def prepare_for_excel(data, value_column_name: str) -> pd.DataFrame:
    # If result is a Series, convert it to DataFrame
    if isinstance(data, pd.Series):
        df_out = data.reset_index()
        df_out.columns = ["State", value_column_name]
        return df_out

    # If result is already a DataFrame, make a copy
    df_out = data.copy()

    # If State is in index, move it into normal column
    if df_out.index.name == "State" or df_out.index.dtype == "object":
        df_out = df_out.reset_index()

    # If first column is not called State, rename it
    if df_out.columns[0] != "State":
        df_out = df_out.rename(columns={df_out.columns[0]: "State"})

    # If DataFrame has only 2 columns, rename second column for cleaner Excel output
    if len(df_out.columns) == 2:
        df_out.columns = ["State", value_column_name]

    return df_out


# Helper function to add a simple bar chart to worksheet
def add_bar_chart(worksheet, chart_title: str, data_title: str) -> None:
    # Create bar chart object
    chart = BarChart()

    # Set chart title and axis titles
    chart.title = chart_title
    chart.y_axis.title = data_title
    chart.x_axis.title = "State"
    chart.style = 10

    # Select data from second column including header
    data = Reference(
        worksheet,
        min_col=2,
        min_row=1,
        max_row=worksheet.max_row
    )

    # Select category names from first column without header
    categories = Reference(
        worksheet,
        min_col=1,
        min_row=2,
        max_row=worksheet.max_row
    )

    # Add data and category labels to chart
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)

    # Add chart into worksheet starting from cell E2
    worksheet.add_chart(chart, "E2")


def main():
    # Create dynamic file path variable to save file path
    file_path = Path(r"C:\Users\Vartotojas\Documents\python\finance.csv")

    # Load data
    df = load_data(file_path)

    # Get info about dataframe
    print("\n--- DATAFRAME INFO ---")
    df.info()

    # Check if there is missing values
    print("\n--- MISSING VALUES ---")
    missing_values = df.isna().sum()
    print(missing_values)

    # Fill missing data with "0"
    # df = df.fillna(0)

    # Delete lines with missing values
    # df = df.dropna()

    # Total revenue per state for all time

    # Group data by state and calculates sum
    all_time = total_revenue_all_time(df)

    print("\nTotal revenue per state (all time):")
    print(all_time)

    # Total revenue per state for 2000–2019
    rev_2000_2019 = total_revenue_between_years(df, 2000, 2019)

    print("\nTotal revenue per state (2000–2019):")
    print(rev_2000_2019)

    # Total revenue in year 2004 for all states
    rev_2004 = total_revenue_for_year(df, 2004)

    print("\nTotal revenue per state in 2004:")
    print(rev_2004)

    # Average interest on debt per state for last 5 years
    avg_interest_last_5 = average_interest_last_n_years(df, 5)

    print("\nAverage interest on debt per state (last 5 years in dataset):")
    print(avg_interest_last_5)

    # Convert all outputs to chart-friendly DataFrames
    all_time_df = prepare_for_excel(all_time, "Totals.Revenue")
    rev_2000_2019_df = prepare_for_excel(rev_2000_2019, "Totals.Revenue")
    rev_2004_df = prepare_for_excel(rev_2004, "Totals.Revenue")
    avg_interest_last_5_df = prepare_for_excel(avg_interest_last_5, "Details.Interest on debt")

    #Create Excel file with multiple sheets
    # Defines output file and resolves file path for easy access
    output_file = Path("finance_analysis_final.xlsx").resolve()

    # creates xlsx file with sheets
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        # Write prepared DataFrames to Excel
        all_time_df.to_excel(writer, sheet_name="All Time Revenue", index=False)
        rev_2000_2019_df.to_excel(writer, sheet_name="Revenue 2000-2019", index=False)
        rev_2004_df.to_excel(writer, sheet_name="Revenue 2004", index=False)
        avg_interest_last_5_df.to_excel(writer, sheet_name="Avg Interest Last 5", index=False)

        # Get worksheet objects from writer
        ws_all_time = writer.sheets["All Time Revenue"]
        ws_2000_2019 = writer.sheets["Revenue 2000-2019"]
        ws_2004 = writer.sheets["Revenue 2004"]
        ws_interest = writer.sheets["Avg Interest Last 5"]

        # Add simple bar chart to each sheet
        add_bar_chart(ws_all_time, "Total Revenue per State (All Time)", "Totals.Revenue")
        add_bar_chart(ws_2000_2019, "Total Revenue per State (2000-2019)", "Totals.Revenue")
        add_bar_chart(ws_2004, "Total Revenue per State (2004)", "Totals.Revenue")
        add_bar_chart(ws_interest, "Average Interest on Debt per State (Last 5 Years)", "Details.Interest on debt")

    print(f"Excel file created successfully at:\n{output_file}")


if __name__ == "__main__":
    main()