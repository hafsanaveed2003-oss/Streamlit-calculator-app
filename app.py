import streamlit as st

st.set_page_config(page_title="Calculator App", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.markdown("Perform basic arithmetic operations!")

num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.success(f"Result: {num1 + num2}")
    elif operation == "Subtract":
        st.success(f"Result: {num1 - num2}")
    elif operation == "Multiply":
        st.success(f"Result: {num1 * num2}")
    elif operation == "Divide":
        if num2 != 0:
            st.success(f"Result: {num1 / num2}")
        else:
            st.error("Cannot divide by zero!")
