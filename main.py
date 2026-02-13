print("starting Real life python task")
#importing path command from pathlib
from pathlib import Path

# Importing pandas for easy data manupulation
import pandas as pd

# Create dynamic file path variable to save file path

file_path = Path(r"C:\Users\Vartotojas\Documents\python\finance.csv")

# Load data
df = pd.read_csv(file_path)

# Ensure Year is numeric
df["Year"] = pd.to_numeric(df["Year"])


# Total revenue per state for all time

# Group data by state and calculates sum
total_revenue_all_time = (df.groupby("State")["Totals.Revenue"]
    .sum()
    .reset_index()
)

print("\nTotal revenue per state (all time):")
print(total_revenue_all_time)


# Total revenue per state for 2000–2019

# Creates required data range set
df_2000_2019 = df[(df["Year"] >= 2000) & (df["Year"] <= 2019)]

# Group data by state and calculates sum
total_revenue_2000_2019 = df_2000_2019.groupby("State")["Totals.Revenue"].sum()

print("\nTotal revenue per state (2000–2019):")
print(total_revenue_2000_2019)


# Total revenue in year 2004 for all states

# Creates required data range set
df_2004 = df[df["Year"] == 2004]

# Group data by state and calculates sum
total_revenue_2004 = df_2004.groupby("State")["Totals.Revenue"].sum()

print("\nTotal revenue per state in 2004:")
print(total_revenue_2004)


# Average interest on debt per state for last 5 years

# Find last 5 years in dataset
last_5_years = sorted(df["Year"].unique())[-5:]

# creates data frame for last five years
df_last_5 = df[df["Year"].isin(last_5_years)]

# calculates average interest on debt per state for last 5 years
average_interest_last_5 = df_last_5.groupby("State")["Details.Interest on debt"].mean()

print("\nAverage interest on debt per state (last 5 years in dataset):")
print(average_interest_last_5)

#Create Excel file with multiple sheets
# Defines output file and resolves file path for easy access
output_file = Path("finance_analysis_final.xlsx").resolve()
# creates xlsx file with sheets
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    total_revenue_all_time.to_excel(writer, sheet_name="All Time Revenue", index=True)
    total_revenue_2000_2019.to_excel(writer, sheet_name="Revenue 2000-2019", index=True)
    total_revenue_2004.to_excel(writer, sheet_name="Revenue 2004", index=True)
    average_interest_last_5.to_excel(writer, sheet_name="Avg Interest Last 5", index=True)

print(f"Excel file created successfully at:\n{output_file}")
