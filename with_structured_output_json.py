from token import OP
from google.generativeai.types import File
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

#schema
# its kinda lengthy , so sir directly pasted and gave a walkthrough of it 

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("The phone is smooth and responsive with a bright display and solid battery life. The camera works well in daylight but struggles at night. Overall, good value for the price")

print(result)

# this might work 