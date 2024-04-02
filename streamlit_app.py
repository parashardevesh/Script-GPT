from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

ai_api_key = os.getenv('OPEN_AI_API_KEY_')
user = OpenAI(api_key=ai_api_key)
gptmodel = 'gpt-3.5-turbo'
userrole = 'user'

pre_prompt = 'Teache me the following concept: '
response = ""

st.title('ProfessorGPT App')
st.divider()
prompt = st.text_input('What do you want to learn?')
gptbutton = st.button('Teach Me')
st.caption('To use ProfessorGPT, Press the button.')
st.divider()

if gptbutton:
    with st.spinner("I am preparing your lecture"):
        response = user.chat.completions.create(
            model= gptmodel,
            messages = [
                {'role': userrole, 'content': pre_prompt+prompt}
            ]
        )
    st.snow()
    st.write(response.choices[0].message.content)
    
