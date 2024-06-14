import streamlit as st
from scipy.stats import norm

def calculate_notional(var_limit, confidence_level, volatility):
    z_score = norm.ppf(confidence_level / 100)
    return var_limit / (z_score * volatility)

st.title("VaR Limit Setting Practice Question")

st.header("Practice Question: Calculate Notional Exposure from VaR Limit")

st.write("1. If the VaR limit is $100,000, the confidence level is 99%, and the volatility is 25%, what is the required notional exposure?")


# Answer input fields for practice questions
st.subheader("Enter your answers below:")

notional_answer1 = st.number_input("Answer for Question 1 (in $)", value=0.0, key="answer1")


if st.button("Submit Answers"):
    correct_answer1 = calculate_notional(100000, 99, 0.25)
    st.write(f"Correct Answer for Question 1: ${correct_answer1:,.2f}")

    
    if notional_answer1 == correct_answer1:
        st.write("Your answer for Question 1 is correct!")
    else:
        st.write(f"Your answer for Question 1 is incorrect.")

