import streamlit as st
# import math
import webbrowser

st.title("Standard Calculator")

first_number = st.text_input("Enter first number", "0")
second_number = st.text_input("Enter second number", "0")


operation = st.selectbox("Select operation:",["Addition", "Substraction", "Multiplication", "Division", "Modulus Division"])

if st.button("Perform Operation"):
	if operation=="Addition":
		result = int (first_number) + int(second_number)
		st.success(f"Your result is {result}")

	elif operation == "Substraction":
		result = int(first_number) - int(second_number) 
		st.success(f"Your result is {result}")

	elif operation =="Multiplication":
		result = int(first_number) * int(second_number)
		st.success(f"Your result is {result}")

	elif operation =="Division":
		result = int(first_number) / int(second_number)
		st.success(f"Your result is {result}")
		
	elif operation == "Modulus Division":
		result = int(first_number) % int(second_number)
		st.success(f"Your result is {result}")


