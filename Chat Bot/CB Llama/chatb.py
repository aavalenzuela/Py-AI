import torch
from transformers import pipeline
import streamlit as st

# Initialize the model
model_id = "meta-llama/Llama-3.2-1B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Create a Streamlit app
st.title("Pirate Chatbot")

# Create a text input for the user
user_input = st.text_input("Talk to the pirate chatbot:", "")

# Create a button to trigger the chatbot response
if st.button("Send"):
    # Define the chatbot's personality
    messages = [
        {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
        {"role": "user", "content": user_input},
    ]

    # Generate the chatbot's response
    outputs = pipe(
        messages,
        max_new_tokens=2048,
    )

    # Display the chatbot's response
    st.write(outputs[0]["generated_text"][2]["content"])
