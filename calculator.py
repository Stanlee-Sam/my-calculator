
import streamlit as st

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Number cannot be divided by 0"
        return num1 / num2
    else:
        return "Invalid Operator"


st.title("Simple Calculator")

num1 = st.number_input("Enter the first number", step=1.0)
num2 = st.number_input("Enter the second number", step=1.0)

operator = st.selectbox(
    "Choose the operator",
    ["+", "-", "*", "/"]
)

if st.button("Calculate"):
    result = calculator(num1, num2, operator)
    st.write("### Result:", result)
