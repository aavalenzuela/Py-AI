Question Answer using DistilBERT and torch

This is a simple Streamlit application to perform question answering with DistilBERT. You can run this Streamlit app locally, where users can input a question and a context, and the app will return the model's answer.

= Instructions to Run the App:

    Install the required packages: Make sure you have streamlit, torch, and transformers installed. You can install them using pip:

    pip install streamlit torch transformers
    
    or
    
    pip install -r requirements.txt



    Run the Streamlit app: In the terminal, navigate to the directory where you saved the app.py file and run the following command:

    streamlit run QADistilBERT.py

    Access the app: Streamlit will open the app in your browser. You can then input a context (paragraph of text) and a question, and click "Get Answer" to see the model’s response.

= How It Works:

    Text Input: The app will allow the user to enter a large block of text (context) and a question.
    Tokenization: The app tokenizes the question and context, and feeds them into the DistilBERT model.
    Model Prediction: The model returns the start and end positions of the answer within the context.
    Answer Extraction: The app extracts and decodes the answer, which is then displayed.
    
= Example:

    **Context:**
    
A Revolution in Perspective

In 1905, Albert Einstein published his theory of special relativity. This theory is discussed in great detail in Relativity in the third volume of this text, so we say only a few words here. In this theory, no motion can exceed the speed of light—it is the speed limit of the Universe. This simple fact has been verified in countless experiments. However, it has incredible consequences—space and time are no longer absolute. Two people moving relative to one another do not agree on the length of objects or the passage of time. Almost all of the mechanics you learned in previous chapters, while remarkably accurate even for speeds of many thousands of miles per second, begin to fail when approaching the speed of light.

This speed limit on the Universe was also a challenge to the inherent assumption in Newton’s law of gravitation that gravity is an action-at-a-distance force. That is, without physical contact, any change in the position of one mass is instantly communicated to all other masses. This assumption does not come from any first principle, as Newton’s theory simply does not address the question. (The same was believed of electromagnetic forces, as well. It is fair to say that most scientists were not completely comfortable with the action-at-a-distance concept.)

A second assumption also appears in Newton’s law of gravitation (Equation). The masses are assumed to be exactly the same as those used in Newton’s second law, $$ \overset{\to }{F}=m\overset{\to }{a}$$. We made that assumption in many of our derivations in this chapter. Again, there is no underlying principle that this must be, but experimental results are consistent with this assumption. In Einstein’s subsequent theory of general relativity (1916), both of these issues were addressed. His theory was a theory of space-time geometry and how mass (and acceleration) distort and interact with that space-time. It was not a theory of gravitational forces. The mathematics of the general theory is beyond the scope of this text, but we can look at some underlying principles and their consequences.


    **Question:**
    What is speed of light?
    
    **Answer:**
    the speed limit of the universe

