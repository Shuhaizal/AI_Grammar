import streamlit as st
from textblob import TextBlob
import time
import os

# Function to paraphrase text
def paraphrase_text(text):
    blob = TextBlob(text)
    return str(blob.correct())

# Main function to create the Streamlit app
def main():
    # Set page title and favicon
    st.set_page_config(page_title="Text Paraphraser", page_icon=":pencil2:")

    # Title and description
    st.title("Text Paraphraser")
    st.markdown(
        """
        Type or paste your text in the box below and click on **Paraphrase** to get a paraphrased version.
        """
    )

    # Full path to the image file
    image_path = os.path.join(os.getcwd(), "para.jpeg")

    # Image representing the system
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=True)
    else:
        st.warning("Image file not found.")

    # Text input area
    input_text = st.text_area("Enter your text here:", height=150)

    # Paraphrase button
    if st.button("Paraphrase"):
        if input_text:
            # Show loading spinner while paraphrasing
            with st.spinner("Paraphrasing..."):
                # Simulate some processing time
                time.sleep(2)
                # Paraphrase the text
                paraphrased_text = paraphrase_text(input_text)
                # Display the paraphrased text
                st.success("Paraphrased Text:")
                st.write(paraphrased_text)
        else:
            st.warning("Please enter some text to paraphrase.")

if __name__ == "__main__":
    main()