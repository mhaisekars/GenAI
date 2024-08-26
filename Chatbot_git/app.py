
import streamlit as st
from langchain_utils import LangchainWrapper
from create_db import DatabaseFactory

#Create Streamlit frontend
st.set_page_config(
    page_title="AI Based SQL Query Assistant"
)

tab_titles=[
    "Results"
]

B_INST,E_INST="[INST]","[/INST]"
db_instance = DatabaseFactory()
db = db_instance.get_engine()
wrapper = LangchainWrapper()
wrapper.create_db_instance(db)
wrapper.create_model()
wrapper.create_chain()

st.title("Your AI Based SQL Query Assistant")
user_input = st.text_input("enter your question")
tabs = st.tabs(tab_titles)

if user_input:
    t2s_result = wrapper.get_response(user_input)
    with tabs[0]:
        st.write(t2s_result)

