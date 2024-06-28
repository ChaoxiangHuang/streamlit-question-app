import streamlit as st
import numpy as np
from scipy.stats import norm

def calculate_notional(var_limit, confidence_level, volatility):
    z_score = norm.ppf(confidence_level / 100)
    return round(var_limit / (z_score * volatility), 2)

st.title("VaR Limit Setting Practice Question")

st.header("Practice Question: Calculate Notional Exposure from VaR Limit")

st.write(f" If the VaR limit is $100,000, the confidence level is 99%, and the volatility is 25%, what is the required notional exposure?")

# Answer input fields for practice questions
st.subheader("Enter your answer below:")

notional_answer = st.text_input(f"Answer for Question (in $)", placeholder="Enter your answer here", key="notional_answer")

if st.button("Submit Answer"):
    correct_answer = calculate_notional(100000, 99, 0.25)
    st.write(f"Correct Answer for Question : ${correct_answer:,.2f}")

    if notional_answer:
        try:
            notional_answer = float(notional_answer)
            if notional_answer == correct_answer:
                st.write(f"Your answer for Question is correct!")
            else:
                st.write(f"Your answer for Question is incorrect.")
        except ValueError:
            st.write("Please enter a valid number.")
    else:
        st.write("Please enter an answer.")

