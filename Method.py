#import os
#os.environ['JAVA_HOME'] = 'C:\\Program Files\\Java\\jdk-11.0.17.8'

import language_tool_python

# Specify the path to the Java executable
java_path = "C:\\Program Files\\Java\\jdk-11.0.17.8\\bin\\java"

import streamlit as st
import language_tool_python

# Initialize LanguageTool
tool = language_tool_python.LanguageTool('en-US')

# Function to perform grammar check
def grammar_check(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# Main function to create the Streamlit app
def main():
    # Set page title
    st.set_page_config(page_title="Grammar Checker")

    # Title and description
    st.title("Grammar Checker")
    st.markdown("""
        Type or paste your text in the box below and click on **Check Grammar** to perform a grammar check.
    """)

    # Text input area
    input_text = st.text_area("Enter your text here:", height=150)

    # Check grammar button
    if st.button("Check Grammar"):
        if input_text:
            # Perform grammar check
            corrected_text = grammar_check(input_text)
            # Display the corrected text
            st.success("Corrected Text:")
            st.write(corrected_text)
        else:
            st.warning("Please enter some text to check grammar.")

if __name__ == "__main__":
    main()
