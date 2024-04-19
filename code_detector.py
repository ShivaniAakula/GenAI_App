import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="CODE DETECTOR",
    page_icon=":mag_right:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        
        'About': "This is Code Detector app.User may detect any python code in the website."
    }
)

# Read API key from file
with open("keys/genaiapp_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title
st.title(":violet[Code Detector with OpenAI]")

# User input section
st.header(":green[Enter Your Python Code]",divider='green')
prompt = st.text_area("Enter your Python code:", height=200)

# Button to trigger code review
if st.button("Review the Code"):
    st.markdown("<h2 style='color:pink;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text