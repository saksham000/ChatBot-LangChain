from langchain.llms import OpenAI
import os 
os.environ["OPENAI_API_KEY"]="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"
llm=OpenAI()
print(llm("Why earth is not flat ?"))
print(os.environ['OPENAI_API_KEY'])