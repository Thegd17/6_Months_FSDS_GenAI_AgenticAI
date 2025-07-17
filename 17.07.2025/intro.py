import streamlit as st 

st.title("My first Streamlit App Created by Gaurav Dhangar")

st.write("This app calculates the square of a number")

# create an interactive slider
st.header("Select a Number")
number = st.slider("Pick a number",0,100,25) # min, max, default

# calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The Square of *{number}* is **{squared_number}**.")