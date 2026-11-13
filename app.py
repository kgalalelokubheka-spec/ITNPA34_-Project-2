
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("research_abstract_classifier.pkl")

# Set up the web page
st.set_page_config(
    page_title="Research Abstract Classifier",
    page_icon="📚",
    layout="centered"
)

st.title("Research Abstract Classifier")

st.write(
    "Enter a research abstract below to classify it as "
    "AI-related or classical research."
)

# Text input area
abstract = st.text_area(
    "Research Abstract",
    placeholder="Paste the research abstract here...",
    height=250
)

# Classify button
if st.button("Classify Abstract"):

    if abstract.strip() == "":
        st.warning("Please enter a research abstract first.")

    else:
        # Predict the category
        prediction = model.predict([abstract])[0]

        st.subheader("Classification Result")

        if prediction == "ai":
            st.success("This abstract is classified as AI-related research.")
        else:
            st.success("This abstract is classified as classical research.")

        st.write("Predicted category:", prediction)
