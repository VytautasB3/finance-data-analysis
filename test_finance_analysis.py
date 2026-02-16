import pandas as pd

from finance_analysis import (
    total_revenue_all_time,
    total_revenue_between_years,
    total_revenue_for_year,
    average_interest_last_n_years,
)

def make_df():
    return pd.DataFrame({
        "State": ["A", "A", "B", "B"],
        "Year":  [2000, 2019, 2004, 2020],
        "Totals.Revenue": [100, 200, 300, 400],
        "Details.Interest on debt": [10, 20, 30, 40],
    })

def test_total_revenue_all_time():
    df = make_df()
    out = total_revenue_all_time(df)
    # out is a DataFrame with columns: State, Totals.Revenue
    a = out.loc[out["State"] == "A", "Totals.Revenue"].iloc[0]
    b = out.loc[out["State"] == "B", "Totals.Revenue"].iloc[0]
    assert a == 300
    assert b == 700

def test_total_revenue_between_years():
    df = make_df()
    out = total_revenue_between_years(df, 2000, 2019)
    assert out["A"] == 300
    assert out["B"] == 300  # only 2004 included, not 2020

def test_total_revenue_for_year():
    df = make_df()
    out = total_revenue_for_year(df, 2004)
    assert out["B"] == 300
    assert "A" not in out.index

def test_average_interest_last_n_years():
    df = make_df()
    out = average_interest_last_n_years(df, n=2)  # last 2 years are 2019 and 2020
    assert out["A"] == 20
    assert out["B"] == 40