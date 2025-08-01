import streamlit as st
import calculator

st.title("Simple Calculator")

operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

result = 0
if st.button("Calculate"):
    if operation == "Add":
        result = calculator.add(num1, num2)
    elif operation == "Subtract":
        result = calculator.subtract(num1, num2)
    elif operation == "Multiply":
        result = calculator.multiply(num1, num2)
    elif operation == "Divide":
        result = calculator.divide(num1, num2)
    st.success(f"The result is {result}")
