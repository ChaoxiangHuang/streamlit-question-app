import streamlit as st

# Question
st.write("### Motivating Question")

question = "How do basic Greeks help in quantifying and describing the risk of linear trades in the equity market?"

# Options for the multiple-choice question
options = [
    "They provide detailed financial statements.",
    "They measure the sensitivity of an option's price to various factors.",
    "They guarantee profits in all trades.",
    "They eliminate all risks in trading."
]

# Display the question
st.write(question)

# Create a radio button for the multiple choice
choice = st.radio("Choose the correct answer:", options)

# Correct answer
correct_answer = options[1]

# Check if the user selected the correct answer
if st.button("Submit"):
    if choice == correct_answer:
        st.success("Correct! Basic Greeks measure the sensitivity of an option's price to various factors.")
    else:
        st.error("Incorrect. Please try again.")
