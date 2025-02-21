import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

# Initialize the tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')

# Streamlit user interface
st.title("Question Answering with DistilBERT")

# Input fields for context and question
context = st.text_area("Enter the context (paragraph):", height=300)
question = st.text_input("Enter your question:")

# When the user presses the button
if st.button("Get Answer"):
    if context and question:
        # Encode the input (tokenize context and question)
        inputs = tokenizer(question, context, return_tensors="pt")

        # Get the model's answer (start and end positions)
        with torch.no_grad():
            outputs = model(**inputs)

        # Extract the answer using the start and end positions
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        # Get the start and end token positions with the highest scores
        start_index = torch.argmax(start_scores)
        end_index = torch.argmax(end_scores)

        # Decode the tokens back to a string (the answer)
        answer_tokens = inputs['input_ids'][0][start_index:end_index + 1]
        answer = tokenizer.decode(answer_tokens)

        # Display the answer
        st.write(f"**Answer:** {answer}")
    else:
        st.warning("Please provide both context and a question.")

