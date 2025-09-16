from token import OP
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

class Review(TypedDict):
    key_themes: Annotated[list[str], "find out key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of what is said in review"]
    sentiment: Annotated[Literal["positive", "negative"], "What is the sentiment of the review - positive or negative"]
    pros: Annotated[Optional[list[str]], "write down all the pros of this product"]
    cons: Annotated[Optional[list[str]], "write down all the cons of this product"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The phone is smooth and responsive with a bright display and solid battery life. The camera works well in daylight but struggles at night. Overall, good value for the price")

print(result)

# This code isnt working i guess because of using gemini , but it will work if you use openai  