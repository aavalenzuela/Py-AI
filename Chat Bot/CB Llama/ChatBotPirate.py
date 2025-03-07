import torch
from transformers import pipeline
import streamlit as st

# Initialize the model
model_id = "meta-llama/Llama-3.2-1B-Instruct"  # Ensure this model exists
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Create a Streamlit app
st.title("Pirate Chatbot")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Construct conversation history as a formatted prompt
    conversation_history = "\n".join(
        [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages]
    )

    # Generate the chatbot's response
    prompt = f"You are a pirate chatbot who always responds in pirate speak!\n\n{conversation_history}\nAssistant:"
    
    outputs = pipe(prompt,
        max_new_tokens=500,
        do_sample=True,
        pad_token_id=pipe.tokenizer.eos_token_id  # Prevents warning Setting `pad_token_id` to `eos_token_id`:None for open-end generation.
    )
    response = outputs[0]["generated_text"].split("Assistant:")[-1].strip()

    with st.chat_message("assistant"):
        st.markdown(response)

    # Store the response in session state
    st.session_state.messages.append({"role": "assistant", "content": response})
