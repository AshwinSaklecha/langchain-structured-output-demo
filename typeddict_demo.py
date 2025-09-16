from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person : Person = {
    'name': "Magnus",
    "age": 34
}

print(new_person)