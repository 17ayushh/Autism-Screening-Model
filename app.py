import streamlit as st
import pickle
import numpy as np

# Load the PCA and trained classifier models using pickle
with open("pca_model.pickle", "rb") as f:
    pca = pickle.load(f)

with open("classifier_model.pickle", "rb") as f:
    model = pickle.load(f)

# Autism screening questions
questions = [
    "I often notice small sounds when others do not?",
    "I find it easy to do more than one thing at once?",
    "I find it easy to read between the lines , when someone is talking to me?",
    "When I'm reading a story I find it difficult to work out the character intentions?",
    "I find it easy to workout what someone is thinking or feeling just by looking at their face?",
    "I usually concentrate more on the whole picture , rather than the small details?",
    "If there was an interruption , I can switch back to what I was doing very quickly?",
    "I know how to tell is someone listening to me is getting bored?",
    "I like to collect information about categories of things?",
    "I find it difficult to work out people's intentions?"
]

# Streamlit UI
st.title("Autism Prediction Chatbot")
st.write("Answer 10 Yes/No questions to check the autism risk.")

# Create input fields
inputs = []
for i, question in enumerate(questions):
    inputs.append(st.selectbox(question, ["Yes", "No"]))

# Convert Yes/No to binary (1/0)
inputs = [1 if ans == "Yes" else 0 for ans in inputs]

# Predict button
if st.button("Predict"):
    # Convert input into numpy array and apply PCA transformation
    new_input_pca = pca.transform([np.array(inputs)])
    
    # Predict using the trained model
    prediction = model.predict(new_input_pca)
     
    # Convert prediction to binary (threshold = 0.5)
    prediction_binary = 1 if prediction[0] >= 0.5 else 0
    
    # Display the result
    st.write(f"Prediction: {'Autistic' if prediction_binary == 1 else 'Not Autistic'}")