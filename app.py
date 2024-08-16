import streamlit as st

# Title of the app
st.title("Welcome to My Streamlit App")

# Subtitle
st.subheader("This is a basic example")

# Write some text
st.write("Hello, this is a simple app to demonstrate how Streamlit works!")

# Adding an interactive widget
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}! Welcome to the app.")

# Adding a slider
slider_value = st.slider("Select a number:", 1, 100)
st.write(f"You selected: {slider_value}")

# Displaying a chart
import numpy as np
import pandas as pd

data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['x', 'y']
)

st.line_chart(data)

# Adding a button
if st.button("Click Me"):
    st.write("Button clicked!")
