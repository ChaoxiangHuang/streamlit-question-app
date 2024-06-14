import streamlit as st
import numpy as np

def calculate_cost_to_liquidate(notional, days_to_liquidate, volatility):
    return (notional / 2) * np.sqrt(days_to_liquidate) * (volatility / 16)

st.title("Cost to Liquidate Practice Question")

st.header("Practice Question: Calculate Cost to Liquidate")


st.write("Given the following inputs, calculate the cost to liquidate:")

notional = st.number_input("Enter Notional Value (in $)", value=1000000.0)
days_to_liquidate = st.number_input("Enter Days to Liquidate", value=5)
volatility = st.number_input("Enter Volatility (in %)", value=20.0) / 100

if st.button("Calculate Cost to Liquidate"):
    cost_to_liquidate = calculate_cost_to_liquidate(notional, days_to_liquidate, volatility)
    st.write(f"Cost to Liquidate: ${cost_to_liquidate:,.2f}")
