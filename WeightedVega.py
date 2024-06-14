import streamlit as st
import numpy as np

def calculate_weighted_vega(base_volatility, maturity_months, base_period_months=3):
    variance_ratio = base_period_months / maturity_months
    weighted_volatility = base_volatility * np.sqrt(variance_ratio)
    return weighted_volatility

st.title("Weighted Vega Practice Question")

st.header("Practice Question: Calculate Weighted Vega")

st.write("""
The standard deviation of the volatility drops in time. That is, the longer the maturity of an asset, the more stable its implied volatility.

An approach to modeling this is to have the variance fall linearly with time. Correspondingly, the standard deviation falls with the square root of time. This linear decay of variance is estimated with respect to a base period, usually 3 months.

For example:
- A 6-month asset's volatility has 1/2 the variance of the 3 months.
- A 1-year asset has 1/4 the variance of the 3-month.
- A 2-year asset, which is made up of 24 months, has 1/8th the variance.

Given the following inputs, calculate the weighted volatility.
""")

# Input fields for the practice question
base_volatility = st.number_input("Enter Base Volatility (in %)", value=20.0) / 100
maturity_months = st.number_input("Enter Maturity in Months", value=6)

if st.button("Calculate Weighted Volatility"):
    weighted_volatility = calculate_weighted_vega(base_volatility, maturity_months)
    st.write(f"Weighted Volatility: {weighted_volatility * 100:.2f}%")
