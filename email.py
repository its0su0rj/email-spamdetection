import streamlit as st

import joblib
import nltk
from nltk.corpus import stopwords

# Set the NLTK data path
#nltk.data.path.append('C:/Users/sujee/Downloads/nltk_data')
nltk.data.path.append('nltk_data')

# Download NLTK resources
#nltk.download('stopwords')

# Load the trained model
model = joblib.load('email_detection_model.joblib')
#model = joblib.load("C:/Users/sujee/Downloads/email_detection_model.joblib")

# Streamlit UI
st.title("Email Spam Detection")

# Input for user to enter an email
user_input = st.text_area("Enter the email text:")

# Button to trigger prediction
if st.button("Check Spam"):
    # Make prediction using the loaded model
    prediction = model.predict([user_input])

    # Display result
    if prediction[0] == 1:
        st.error("This email is classified as spam.")
    else:
        st.success("This email is not classified as spam.")
