import streamlit as st
import numpy as np

def annual_to_daily_vol(annual_vol):
    return round(annual_vol / 16, 2)

st.title("VaR Rule of 16 Drill App")

st.header("Estimating Daily Volatility from Annual Volatility")

st.write("""
There are approximately 252 trading days in a year. To adjust from annual volatility to daily volatility, we divide by the square root of 252. Since sqrt(252) ≈ 15.88, we approximate that with 16. This allows us to estimate daily volatility using simple arithmetic.
""")

# Generate random annual volatilities
np.random.seed()  # Reset the seed for random number generation
annual_vol_1 = round(np.random.uniform(10, 50), 2)
annual_vol_2 = round(np.random.uniform(10, 50), 2)
annual_vol_3 = round(np.random.uniform(10, 50), 2)

annual_vols = [annual_vol_1, annual_vol_2, annual_vol_3]

for i, annual_vol in enumerate(annual_vols, 1):
    st.write(f"Annual Volatility {i}: {annual_vol}%")
    user_input = st.text_input(f"Enter your calculated Daily Volatility for Annual Volatility {i}:", key=f"user_input_{i}",placeholder=f"Enter your answer here")
    if st.button(f"Check Answer for Volatility {i}", key=f"check_answer_{i}"):
        correct_answer = annual_to_daily_vol(annual_vol)
        if user_input:
            user_input = float(user_input)
            if user_input == correct_answer:
                st.write(f"Correct! Daily Volatility is {correct_answer}%")
            else:
                st.write(f"Incorrect. The correct Daily Volatility is {correct_answer}%")
        else:
            st.write("Please enter an answer.")

