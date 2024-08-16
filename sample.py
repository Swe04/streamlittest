import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Initialize Faker to generate synthetic data
faker = Faker()

# Function to generate sample patient data
def generate_patient_data(num_patients=100):
    data = {
        "Patient ID": [faker.random_number(digits=6, fix_len=True) for _ in range(num_patients)],
        "Name": [faker.name() for _ in range(num_patients)],
        "Age": [np.random.randint(0, 100) for _ in range(num_patients)],
        "Gender": [np.random.choice(["Male", "Female"]) for _ in range(num_patients)],
        "Disease": [np.random.choice(["Heart Disease", "Diabetes", "Cancer", "Asthma", "Covid-19", "Flu"]) for _ in range(num_patients)],
        "Severity": [np.random.choice(["Mild", "Moderate", "Severe", "Critical"]) for _ in range(num_patients)],
        "Admission Date": [faker.date_between(start_date='-1y', end_date='today') for _ in range(num_patients)],
        "Discharge Date": [faker.date_between(start_date='today', end_date='+30d') for _ in range(num_patients)],
        "Doctor": [faker.name() for _ in range(num_patients)],
        "Room Availability": [np.random.choice(["Available", "Occupied"]) for _ in range(num_patients)],
        "Bed Availability": [np.random.choice(["Available", "Occupied"]) for _ in range(num_patients)],
        "Risk Factor": [np.random.choice(["Low", "Moderate", "High"]) for _ in range(num_patients)],
        "Follow-Up Required": [np.random.choice(["Yes", "No"]) for _ in range(num_patients)],
        "Insurance Coverage": [np.random.choice(["Yes", "No"]) for _ in range(num_patients)]
    }
    return pd.DataFrame(data)

# Function to display patient data
def display_patient_data():
    st.title("Patient Care Analysis and Outreach")
    st.subheader("Patient Data Overview")
    
    num_patients = st.slider("Select number of patients to view", 10, 1000, 100)
    patient_data = generate_patient_data(num_patients)
    
    st.dataframe(patient_data)
    
    return patient_data

# Function to create and display charts
def display_charts(patient_data):
    st.subheader("Patient Data Visualizations")

    # Gender distribution
    gender_count = patient_data["Gender"].value_counts()
    st.write("### Gender Distribution")
    st.bar_chart(gender_count)
    
    # Age distribution
    st.write("### Age Distribution")
    fig, ax = plt.subplots()
    ax.hist(patient_data["Age"], bins=20, color='skyblue', edgecolor='black')
    st.pyplot(fig)
    
    # Disease distribution
    st.write("### Disease Distribution")
    disease_count = patient_data["Disease"].value_counts()
    fig_disease = px.pie(names=disease_count.index, values=disease_count.values, title="Disease Distribution")
    st.plotly_chart(fig_disease)
    
    # Severity distribution
    st.write("### Severity of Illness")
    severity_count = patient_data["Severity"].value_counts()
    fig_severity = px.bar(severity_count, x=severity_count.index, y=severity_count.values, title="Severity of Illness")
    st.plotly_chart(fig_severity)
    
    # Room and Bed Availability
    st.write("### Room and Bed Availability")
    room_bed_count = pd.DataFrame({
        'Room Availability': patient_data["Room Availability"].value_counts(),
        'Bed Availability': patient_data["Bed Availability"].value_counts()
    })
    st.bar_chart(room_bed_count)

# Function to simulate a predictive model interface
def predictive_model_interface():
    st.subheader("Disease Severity Prediction")
    
    # Sample input fields
    age = st.number_input("Age", min_value=0, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female"])
    disease = st.selectbox("Disease", ["Heart Disease", "Diabetes", "Cancer", "Asthma", "Covid-19", "Flu"])
    risk_factor = st.selectbox("Risk Factor", ["Low", "Moderate", "High"])
    
    if st.button("Predict Severity"):
        # Placeholder for predictive model (replace with actual model)
        severity = np.random.choice(["Mild", "Moderate", "Severe", "Critical"])
        st.success(f"Predicted Severity: {severity}")

# Function to manage hospital resources
def resource_management():
    st.subheader("Hospital Resource Management")
    
    room_availability = np.random.choice(["Available", "Occupied"], size=5)
    bed_availability = np.random.choice(["Available", "Occupied"], size=5)
    
    st.write("Room Availability:")
    st.write(room_availability)
    
    st.write("Bed Availability:")
    st.write(bed_availability)

# Function to embed KoreAI chatbot
def embed_chatbot():
    chatbot_code = """
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
    components.html(chatbot_code, height=600)

# Main application
st.sidebar.title("Navigation")
menu = ["Patient Data", "Predictive Model", "Resource Management", "Patient Data Dashboard", "Chatbot"]
choice = st.sidebar.selectbox("Select a page", menu)

if choice == "Patient Data":
    patient_data = display_patient_data()
elif choice == "Predictive Model":
    predictive_model_interface()
elif choice == "Resource Management":
    resource_management()
elif choice == "Patient Data Dashboard":
    patient_data = display_patient_data()
    display_charts(patient_data)
elif choice == "Chatbot":
    embed_chatbot()
