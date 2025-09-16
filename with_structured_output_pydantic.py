from token import OP
from google.generativeai.types import File
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

#schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="find out key themes discussed in the review")
    # key_themes: Annotated[list[str], "find out key themes discussed in the review"]
    summary: str = Field(description="A brief summary of what is said in review")
    # summary: Annotated[str, "A brief summary of what is said in review"]
    sentiment: Literal["positive", "negative"] = Field(description="copypaste")
    # sentiment: Annotated[Literal["positive", "negative"], "What is the sentiment of the review - positive or negative"]
    pros: Optional[list[str]] = Field(default=None, description="copypaste")
    # pros: Annotated[Optional[list[str]], "write down all the pros of this product"]
    cons: Optional[list[str]] = Field(default=None, description="copypaste")
    # cons: Annotated[Optional[list[str]], "write down all the cons of this product"]


structured_model = model.with_structured_output(Review)
result = structured_model.invoke("The phone is smooth and responsive with a bright display and solid battery life. The camera works well in daylight but struggles at night. Overall, good value for the price")

print(result)

# this might work 