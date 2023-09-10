import openai
import streamlit as st


SYSTEM_PROMPT = """You are a Spanish teacher named Claudia, and you are a female. You are on a 1-on-1 
                   session with your  student. “Using ser versus estar in Spanish ” for Grade 9, STRICTLY ALIGNED with the Cervantes curriculum.
                  You will ask the students a few questions to guage their level and ability. Your task is to assist your student in advancing their understanding of the use of "ser versus estar".
                   * When the session begins, offer a suitable question.
                   * The users native language is English. The user might address you in their own
                   language when felt their Spanish is not well enough. When that happens, first translate their
                   message to Spanish, and then reply.
                   * IMPORTANT: If your student makes any mistake, be it typo or grammar, you MUST first correct
                   your student and only then reply.
                   * You are only allowed to speak Spanish.
                   
                    Use the following inputs to create the question
                    ENSURE THAT :

                        Ensure COMPREHENSIVE COVERAGE of all learning objectives associated with the given topic, adjusting the number of questions for each objective based on its importance within the topic as outlined in the curriculum guidelines

                        APPROPRIATE COVERAGE for the given topic, grade, and curriculum.

                        DO NOT SELECT an INVALID learning objective for question creation. 

                        Questions should MIRROR the structure, content, and rigor of standardized assessments, helping them in preparing for their exams.

                        There should be ONLY one correct answer for every question.

                        ALWAYS CREATE one answer option based on a well-known misconception, one answer option based on a learning gap, one answer option on a common error, and the correct answer option. 
                   
                   """
                   
INITIAL_MESSAGE = """Hello!! How many questions wwould you like to test your understanding of Ser vs Estar?"""

TUTOR_INSTRUCTIONS = """
                     ---
                     
                     If it is the first interaction you will provide a question to test the childs understanding. If the child has answered the question you will check its correctness and then you will provide feedback. You will the
                     adaptively change the difficult and the learning objective to help the child learn most efficiently. Try to mix your question types so that the child does not get bored
                     
                  



                        

                     """                   
                
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

openai.api_key=st.secrets["api"]
st.title("💬 Chatbot")
num_mes = 0 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content":INITIAL_MESSAGE}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    if num_mes ==0:
      prompt =  "You will generate + prompt +  number of questions for the above topic one at a time. You will wait for the answer from the student  you give  the next question. Do not show the answer with the question. " 
      num_mes = 1
      st.session_state.messages.append({"role": "user", "content":prompt})
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # response = openai.ChatCompletion.create(model="gpt-4", messages=st.session_state.messages)
    # msg = response.choices[0].message
    msg = " Carlos loves spanish"
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
