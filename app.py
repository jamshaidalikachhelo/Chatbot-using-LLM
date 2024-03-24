import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import os
#os.environ["OPEN_API_KEY"]="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"

load_dotenv()

# function to load OpenAI and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-0613", temperature=0.5)
    response = llm(question)
    return response

# initialize our Streamlit app
st.set_page_config(page_title="chatbot")
st.header("SIMPLE LANGCHAIN APPLICATION")

# Get user input
input_question = st.text_input("Input: ", key="input")

# Display response when user clicks the "Ask" button
if st.button("Ask The Question"):
    response = get_openai_response(input_question)
    st.subheader("The Response Is")
    st.write(response)
