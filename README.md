# Finance Data Analysis

A small Python project for analyzing financial data from a CSV file and exporting the results to an Excel workbook with charts.

The project demonstrates basic data manipulation with pandas, reusable Python functions, automated testing with pytest, and Excel report generation with openpyxl.

## Features

The project performs the following analyses:

* Calculates total revenue per state across all available years.
* Calculates total revenue per state for a selected year range.
* Calculates total revenue per state for a specific year.
* Calculates average interest on debt per state for the last N years available in the dataset.
* Checks the dataset for missing values.
* Exports analysis results into a multi-sheet Excel workbook.
* Adds bar charts to the generated Excel sheets.

## Technologies

* Python
* pandas
* openpyxl
* pytest
* Git

## Project Structure

```text
csv_project/
├── data_analysis.py
├── main.py
├── test_data_analysis.py
├── finance.csv
├── requirements.txt
├── README.md
└── .gitignore
```

### `data_analysis.py`

Contains reusable functions for loading and analyzing the financial dataset.

### `main.py`

Runs the analysis, checks the dataset, prepares the results, and generates the final Excel report.

### `test_data_analysis.py`

Contains automated tests for the data analysis functions using pytest.

## Installation

Clone the repository and navigate to the project directory.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Running the Project

Run:

```powershell
python main.py
```

The program reads `finance.csv`, performs the financial analysis, and generates:

```text
finance_analysis_final.xlsx
```

The Excel file contains separate worksheets for each analysis together with bar charts.

## Running Tests

Run the automated tests with:

```powershell
pytest
```

## Analysis Functions

The main analysis functions include:

```python
total_revenue_all_time(df)
total_revenue_between_years(df, start, end)
total_revenue_for_year(df, year)
average_interest_last_n_years(df, n)
```

These functions separate the core data analysis logic from the reporting logic in `main.py`.

## Purpose

This project was created as a practical exercise in Python data processing and demonstrates fundamental concepts useful in data engineering, including data ingestion, transformation, aggregation, testing, and output generation.
