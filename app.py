import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

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
data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['x', 'y']
)
st.line_chart(data)

# Adding a button
if st.button("Click Me"):
    st.write("Button clicked!")

# Embed Kore.ai Chatbot
chatbot_html = """
<link rel='stylesheet' href='https://bots.kore.ai/webclient/UI/dist/kore-ai-sdk.min.css'></link>
<script src='https://bots.kore.ai/api/platform/websdkjs/ce2c77b5242f4711bcb59a2dc1cb55d3be4f0456fa79428e834c982c3c383a50st22'></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        if (window.KoreSDK) {
            KoreSDK.show(KoreSDK.chatConfig);
        } else {
            console.error("KoreSDK is not loaded");
        }
    });
</script>
"""

# Embed the chatbot HTML in Streamlit
components.html(chatbot_html, height=600)
