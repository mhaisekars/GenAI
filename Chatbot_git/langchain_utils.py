from langchain_community.utilities import SQLDatabase
from operator import itemgetter
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.llms import LlamaCpp
from langchain.memory import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from config import app_config
from prompts import final_prompt,answer_prompt
from utilities import response_without_prefix

class LangchainWrapper:
    def __init__(self):
        self.db = None
        self.history = ChatMessageHistory()
        self.llm = None
        self.chain = None

    def create_db_instance(self, engine):
        self.db = SQLDatabase(engine=engine) if self.db is None else self.db
        return self.db
    
    def create_model(self):
        if self.llm is None:
            n_gpu_layers = app_config.n_gpu_layers
            n_batch = app_config.n_batch
            # Make sure the model path is correct for your system!
            #self.llm = LlamaCpp(
            #    model_path="./models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
            #    n_gpu_layers=n_gpu_layers,
            #    n_batch=n_batch,
            #    temperature=0,
            #    top_k = 2,
            #    n_ctx=2048,
            #    f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
            #    verbose=True,
            #)
            self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        return self.llm

    def create_chain(self):
        if self.chain is None:
            generate_query = create_sql_query_chain(self.llm, self.db,final_prompt)
            execute_query = response_without_prefix|QuerySQLDataBaseTool(db=self.db)
            rephrase_answer = answer_prompt | self.llm | StrOutputParser()
            self.chain = (
                    RunnablePassthrough.assign(query=generate_query).assign(
                        result=itemgetter("query") | execute_query
                    )
                    | rephrase_answer
                    )
        return self.chain
    
    def get_response(self, question):
        response = self.chain.invoke({"question": question,"messages":self.history.messages})
        self.history.add_user_message(question)
        self.history.add_ai_message(response)
        return response