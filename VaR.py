import streamlit as st
import numpy as np
from scipy.stats import norm

def calculate_var(volatility, confidence_level):
    if confidence_level == 95:
        z_score = 1.64
    elif confidence_level == 98:
        z_score = 2.05
    elif confidence_level == 99:
        z_score = 2.33
    elif confidence_level == 99.5:
        z_score = 2.58
    elif confidence_level == 99.9:
        z_score = 3.09
    else:
        z_score = norm.ppf(confidence_level / 100)
    return round(volatility * z_score, 2)

st.header("Practice Questions")

# Generate random volatilities
np.random.seed()  # Reset the seed for random number generation
practice_vol_1 = round(np.random.uniform(10, 50))
practice_vol_2 = round(np.random.uniform(10, 50))

# Randomly select confidence levels
confidence_levels = [95, 98, 99, 99.5, 99.9]
practice_conf_level_1 = np.random.choice(confidence_levels)
practice_conf_level_2 = np.random.choice(confidence_levels)

practice_data = [
    (practice_vol_1, practice_conf_level_1),
    (practice_vol_2, practice_conf_level_2)
]

for i, (practice_vol, practice_conf_level) in enumerate(practice_data, 1):
    st.write(f"**Question {i}:**")
    st.write(f"Annual Volatility: {practice_vol}%")
    st.write(f"Confidence Level: {practice_conf_level}%")
    user_input = st.text_input(f"Enter your calculated VaR for Annual Volatility {i}:", key=f"user_input_{i}", placeholder="Enter your answer here")
    if st.button(f"Check Answer for Volatility {i}", key=f"check_answer_{i}"):
        correct_answer = calculate_var(practice_vol, practice_conf_level)
        if user_input and user_input != "Enter your answer here":
            user_input = float(user_input)
            if user_input == correct_answer:
                st.write(f"Correct! VaR is {correct_answer}%")
            else:
                st.write(f"Incorrect. The correct VaR is {correct_answer}%")
        else:
            st.write("Please enter an answer.")
    
    st.write("---")  # Add a horizontal line for spacing between questions
