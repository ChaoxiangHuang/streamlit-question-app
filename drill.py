import streamlit as st
import numpy as np

def calculate_beta(cov_x_spx, var_spx):
    return cov_x_spx / var_spx

def calculate_adjusted_beta(correlation, vol_x, vol_spx):
    return correlation * (vol_x / vol_spx)

st.title("Beta Adjusted Delta Drill App")

st.header("Simple Example for Beta Calculation")

# Example 1: Basic Beta Calculation
st.subheader("Example 1: Basic Beta Calculation")
cov_x_spx = st.number_input("Enter Covariance between Asset (X) and Market (SPX)", value=0.02)
var_spx = st.number_input("Enter Variance of the Market (SPX)", value=0.04)
if st.button("Calculate Beta"):
    beta = calculate_beta(cov_x_spx, var_spx)
    st.write(f"Beta: {beta}")

# Example 2: Adjusted Beta Calculation
st.subheader("Example 2: Adjusted Beta Calculation")
correlation = st.number_input("Enter Correlation (ρ) between Asset (X) and Market (SPX)", value=0.5)
vol_x = st.number_input("Enter Volatility of Asset (X)", value=0.3)
vol_spx = st.number_input("Enter Volatility of Market (SPX)", value=0.2)
if st.button("Calculate Adjusted Beta"):
    adjusted_beta = calculate_adjusted_beta(correlation, vol_x, vol_spx)
    st.write(f"Adjusted Beta: {adjusted_beta}")

# Thought Question Example
st.subheader("Thought Question Example")
st.write("An idiosyncratic event specific to a company has doubled its volatility. Mathematically, what would happen to its beta?")
initial_beta = st.number_input("Enter Initial Beta", value=1.0)
initial_vol_x = st.number_input("Enter Initial Volatility of Asset (X)", value=0.3)
new_vol_x = st.number_input("Enter New Volatility of Asset (X) (after the event)", value=0.6)
initial_correlation = st.number_input("Enter Initial Correlation (ρ) between Asset (X) and Market (SPX)", value=0.5)
if st.button("Calculate New Beta"):
    new_beta = initial_beta * (new_vol_x / initial_vol_x)
    st.write(f"New Beta (assuming correlation stays the same): {new_beta}")
    st.write("To keep the beta value the same after the volatility of X has doubled, the correlation must decrease.")
    new_correlation = initial_correlation * (initial_vol_x / new_vol_x)
    st.write(f"New Correlation (to keep Beta same): {new_correlation}")
