import streamlit as st
from textblob import TextBlob
import time

# Function to paraphrase text
def paraphrase_text(text):
    blob = TextBlob(text)
    return str(blob.correct())

# Main function to create the Streamlit app
def main():
    # Set page title and favicon
    st.set_page_config(page_title="Text Paraphraser", page_icon=":pencil2:")

    # CSS styling for the interface
    st.markdown(
        """
        <style>
        .st-eb {
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #ccc;
        }
        .st-dg, .st-dh, .st-ef {
            border-radius: 10px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
        .st-eb:hover {
            border-color: #888;
        }
        .st-dg, .st-dh, .st-ef:hover {
            box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and description
    st.title("Text Paraphraser")
    st.markdown(
        """
        Type or paste your text in the box below and click on **Paraphrase** to get a paraphrased version.
        """
    )

    # Image representing the system
    st.image("paraphraser_image.jpg", use_column_width=True)

    # Text input area
    input_text = st.text_area("Enter your text here:", height=150)

    # Paraphrase button with custom styling
    if st.button("Paraphrase", key="paraphrase_button"):
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