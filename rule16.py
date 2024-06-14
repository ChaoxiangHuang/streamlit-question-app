import streamlit as st
import numpy as np

def annual_to_daily_vol(annual_vol):
    return annual_vol / 16

st.title("VaR Rule of 16 Drill App")

st.header("Estimating Daily Volatility from Annual Volatility")

st.write("""
There are approximately 252 trading days in a year. To adjust from annual volatility to daily volatility, we divide by the square root of 252. Since sqrt(252) ≈ 15.88, we approximate that with 16. This allows us to estimate daily volatility using simple arithmetic.
""")

# Example 1: Calculation
st.subheader("Example 1: Calculate Daily Volatility")
annual_vol = st.number_input("Enter Annual Volatility (in %)", value=16.0)
if st.button("Calculate Daily Volatility"):
    daily_vol = annual_to_daily_vol(annual_vol)
    st.write(f"Daily Volatility: {daily_vol}%")

# Practice Questions
st.subheader("Practice Questions")
st.write("Try to calculate the daily volatility for the given annual volatilities:")

annual_vol_1 = 16.0
annual_vol_2 = 24.0
annual_vol_3 = 32.0

if st.button("Show Practice Answers"):
    daily_vol_1 = annual_to_daily_vol(annual_vol_1)
    daily_vol_2 = annual_to_daily_vol(annual_vol_2)
    daily_vol_3 = annual_to_daily_vol(annual_vol_3)
    st.write(f"Annual Volatility: {annual_vol_1}% 🡪 Daily Volatility: {daily_vol_1}%")
    st.write(f"Annual Volatility: {annual_vol_2}% 🡪 Daily Volatility: {daily_vol_2}%")
    st.write(f"Annual Volatility: {annual_vol_3}% 🡪 Daily Volatility: {daily_vol_3}%")

# Thought Question
st.subheader("Thought Question")
st.write("If an asset has an annual volatility of 40%, what would be its daily volatility using the rule of 16?")
annual_vol_question = 40.0
if st.button("Show Answer for Thought Question"):
    daily_vol_question = annual_to_daily_vol(annual_vol_question)
    st.write(f"Annual Volatility: {annual_vol_question}% 🡪 Daily Volatility: {daily_vol_question}%")

