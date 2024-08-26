from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,FewShotChatMessagePromptTemplate,PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from templates.training_examples import examples

from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}\nSQLQuery:"),
        ("ai", "{query}"),
    ]
)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    # input_variables=["input","top_k"],
    input_variables=["input","top_k"],
)

few_shot_selector_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    example_selector=SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(),
        Chroma,
        k=2,
        input_keys=["input"],
    ),
    # input_variables=["input","top_k"],
    input_variables=["input","top_k"],
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. \n\nHere is the relevant table info: {table_info}\n\nBelow are a number of examples of questions and their corresponding SQL queries. Ignore the 'AI: ' prefix in these examples. It is used to indicate that it was response from model. your answer should contain only the query without prefix. Check your generated answer if it contains 'AI:' prefix, remove it before responding."),
        few_shot_prompt,
        MessagesPlaceholder(variable_name="messages"),
        ("human", "{input}"),
    ]
)

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
if the response is single value, use it in sentence.
if the response is table, use it in table format.
Add the SQL query before the above result. remove AI: prefix while adding it.

example:
Question: "How many passengers do we have?"
SQL Query: AI: SELECT COUNT(*) FROM passengers;
SQL Result: [(123,)]
Answer: We have 123 passengers.

Question: "What is the total fare for the trip with trip id 1234?"
SQL Query: AI: SELECT total_amount FROM trips WHERE trip_id = 1234;
SQL Result: [(100.5,)]
Answer: The total fare for trip id 1234 is 100.5.

Question: "What is full name of passenger Jacob Milling?"
SQL Query: AI: SELECT name FROM passengers WHERE name = '%Jacob%Milling';
SQL Result: [('Mr. Jacob Christian Milling',)]
Answer: Mr. Jacob Christian Milling is the full name of passenger Jacob Milling.

Question: "Give distribution of the survivors by age?"
SQL Query: AI: SELECT age, count(*) FROM passengers WHERE survived = 1 GROUP BY age;
SQL Result: [(10, 10), (20, 20), (30, 30), (40, 40), (50, 50)]
Answer: The distribution of survivors by age is as follows:
        Age | Count
        10 | 10
        20 | 20
        30 | 30
        40 | 40
        50 | 50

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)