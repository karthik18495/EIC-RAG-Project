from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser



# Creating a Runnable Branch
# Query -> Decide -> Generate or RAG chain

def DecideAndRunChain(llm):
    decide_prompt = PromptTemplate.from_template("Templates/Decide_Prompts/decide_prompt_00.template")
    decide_chain = decide_prompt | llm | StrOutputParser()
    
    RAG_chain = 