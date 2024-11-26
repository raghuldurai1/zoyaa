import streamlit as st
import cohere
import os

# Initialize the Cohere client with your API key from an environment variable
  # Replace with actual key or ensure the env variable is set
cohere_client = cohere.Client('wP6gwqGMQMWvJZmy3YunEs5NiNwMmzVwn2mYu7pS')

# Helper functions
def generate_code(language, task):
    try:
        prompt = f"Generate a simple {language} code to {task}."
        response = cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=150,
            temperature=0.5
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error generating code: {e}"

def debug_code(code):
    try:
        prompt = f"The following code has an issue. Provide debugging suggestions:\n{code}"
        response = cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=150,
            temperature=0.5
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error debugging code: {e}"

# Streamlit interface
st.title('Code Generator and Debugger')

# Code Generation Section
st.subheader('Generate Code')
language = st.selectbox(
    "Select programming language",
    ["Python", "JavaScript", "C++", "Java", "C#", "C", "SQL", "HTML", "CSS"]
)
task = st.text_input("Describe the task (e.g., 'calculate factorial of a number')")

if st.button('Generate Code'):
    if task:
        code = generate_code(language, task)
        st.text_area("Generated Code", value=code, height=200)
    else:
        st.warning("Please enter a task description!")

# Code Debugging Section
st.subheader('Debug Code')
code_to_debug = st.text_area("Paste the code you want to debug")

if st.button('Debug Code'):
    if code_to_debug.strip():
        debug_suggestions = debug_code(code_to_debug)
        st.text_area("Debugging Suggestions", value=debug_suggestions, height=200)
    else:
        st.warning("Please paste some code to debug!")
