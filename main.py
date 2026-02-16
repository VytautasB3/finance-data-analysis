print("Starting Real life python task")
#importing path command from pathlib
from pathlib import Path

# Importing pandas for easy data manupulation
import pandas as pd

# Importing function from fynance_analysis
from finance_analysis import (
    load_data,
    total_revenue_all_time,
    total_revenue_between_years,
    total_revenue_for_year,
    average_interest_last_n_years,
)

def main():
    # Create dynamic file path variable to save file path
    file_path = Path(r"C:\Users\Vartotojas\Documents\python\finance.csv")

    # Load data
    df = load_data(file_path)

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

    #Create Excel file with multiple sheets
    # Defines output file and resolves file path for easy access
    output_file = Path("finance_analysis_final.xlsx").resolve()

    # creates xlsx file with sheets
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        all_time.to_excel(writer, sheet_name="All Time Revenue", index=False)
        rev_2000_2019.to_frame(name="Totals.Revenue").to_excel(
            writer, sheet_name="Revenue 2000-2019", index=True
        )
        rev_2004.to_frame(name="Totals.Revenue").to_excel(
            writer, sheet_name="Revenue 2004", index=True
        )
        avg_interest_last_5.to_frame(name="Details.Interest on debt").to_excel(
            writer, sheet_name="Avg Interest Last 5", index=True
        )

    print(f"Excel file created successfully at:\n{output_file}")

if __name__ == "__main__":
    main()