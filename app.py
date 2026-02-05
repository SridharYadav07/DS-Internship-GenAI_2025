import streamlit as st
import joblib
import re

# Load trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.set_page_config(page_title="Flipkart Sentiment Analysis")

st.title("Flipkart Product Review Sentiment Analysis")
st.write("Enter a product review below to predict its sentiment.")

# Text input
review = st.text_area("Review Text")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

# Predict button
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        cleaned_review = clean_text(review)
        vector = vectorizer.transform([cleaned_review])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.success("Positive Review")
        else:
            st.error("Negative Review")