import streamlit as st 
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("This is a simple app to demonstrate the basic functionalities of streamlit.")

st.sidebar.header("User Input Features")

# text input
user_name = st.sidebar.text_input("What is your name?","Streamlit User")

# silder
age = st.sidebar.slider("Select Your Age",0,100,25)

# selection
fav_color = st.sidebar.selectbox("What is your favorite color?",["Blue","Red","Green","Yellow","Orange"])

# Main page
st.header(f"Welcome,{user_name}")
st.write(f"You are {age} years old and your favorite color is {fav_color}.")

# displayng data
st.subheader("Here's some randomm data:")

# create a sample dataframe
data = pd.DataFrame(
    np.random.randn(10,5),
    columns=('col %d' %i for i in range(5))
)

st.dataframe(data)

# checkbox to show/hide content``
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)
    
# Button to trigger an action
if st.button("Say Hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye!")