from pathlib import Path
import pandas as pd

#Loading data from path
def load_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df["Year"] = pd.to_numeric(df["Year"])
    return df


def total_revenue_all_time(df: pd.DataFrame):
    return (
        df.groupby("State")["Totals.Revenue"]
        .sum()
        .reset_index()
    )


def total_revenue_between_years(df: pd.DataFrame, start: int, end: int):
    filtered = df[(df["Year"] >= start) & (df["Year"] <= end)]
    return filtered.groupby("State")["Totals.Revenue"].sum()


def total_revenue_for_year(df: pd.DataFrame, year: int):
    filtered = df[df["Year"] == year]
    return filtered.groupby("State")["Totals.Revenue"].sum()


def average_interest_last_n_years(df: pd.DataFrame, n: int = 5):
    last_years = sorted(df["Year"].unique())[-n:]
    filtered = df[df["Year"].isin(last_years)]
    return filtered.groupby("State")["Details.Interest on debt"].mean()