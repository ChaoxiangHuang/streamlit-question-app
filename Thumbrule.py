import streamlit as st
import numpy as np

def calculate_atm_call_option(volatility, time_to_maturity, notional):
    return 0.4 * volatility * np.sqrt(time_to_maturity) * notional

st.title("ATM Call Option Value Practice Question")

st.header("Practice Question: Calculate ATM Call Option Value")

st.write("""
Given the following inputs, calculate the ATM call option value.
""")

# Input fields for the practice question
volatility = st.number_input("Enter Volatility (in %)", value=20.0) / 100
time_to_maturity = st.number_input("Enter Time to Maturity (in years)", value=1.0)
notional = st.number_input("Enter Notional Value (in $)", value=1000000.0)

if st.button("Calculate ATM Call Option Value"):
    atm_call_value = calculate_atm_call_option(volatility, time_to_maturity, notional)
    st.write(f"ATM Call Option Value: ${atm_call_value:,.2f}")
