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
    return volatility * z_score

st.title("VaR Drill App")

st.header("VaR as Survival Capital and Bad Day")

st.write("""
**VaR (Value at Risk)** represents the amount of capital required to survive an adverse event. The degree of adversity can be expressed in terms of its infrequency, similar to weather events (e.g., 1-in-5-year storms).
""")

st.write("""
**VaR as a Bad Day**: We can build our intuition on how frequently bad days occur by relating probability to time.

- A 95th percentile event occurs once every 20 days (about once a month).
- A 98th percentile event occurs once every 50 days (about once every 2.5 months).
- A 99th percentile event occurs once every 100 days (about once every 5 months).

Annual frequencies:
- 95th percentile event occurs about 13 times per year.
- 98th percentile event occurs about 6 times per year.
- 99th percentile event occurs about 3 times per year.
""")

st.header("VaR Estimation Practice")

# Input for volatility and confidence level
volatility = st.number_input("Enter Volatility (in %)", value=16.0)
confidence_level = st.selectbox("Select Confidence Level (in %)", [95, 98, 99, 99.5, 99.9])

if st.button("Calculate VaR"):
    var_value = calculate_var(volatility, confidence_level)
    st.write(f"VaR at {confidence_level}% confidence level: {var_value}%")

st.header("Thought Questions")

st.write("""
1. **Risk Appetite and VaR**: Explain how a company might use VaR to express its risk appetite and set risk limits.
2. **VaR and Delta Exposure**: Describe how VaR can be defined over different time horizons and how it translates from risk appetite to Delta Exposure.
3. **Confidence Levels and Data**: Discuss the usefulness of interpreting VaR as a bad day if data to support confidence levels of 99% and above is lacking.
""")

st.header("Confidence Level to Standard Deviations")

confidence_levels = {
    95: "1.64 ≈ 1 + 2/3 = 5/3",
    98: "2.05 ≈ 2",
    99: "2.33 ≈ 2 + 1/3 = 7/3",
    99.5: "2.58 ≈ 2.5",
    99.9: "3.09 ≈ 3"
}

st.write("The following are approximate conversions from confidence levels to standard deviations:")
for level, conversion in confidence_levels.items():
    st.write(f"{level}% = {conversion}")

st.header("Practice Questions with Answers")

if st.button("Show Practice Answers"):
    for level, conversion in confidence_levels.items():
        st.write(f"{level}% confidence level corresponds to {conversion} standard deviations")

