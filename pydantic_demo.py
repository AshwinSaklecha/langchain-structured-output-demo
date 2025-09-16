from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str = "Nodirbek"
    age: Optional[int] = None # why to put optional if we are putting None here?
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default= 5.5, description="A decimal value representing cgpa")


student = Student(name="Magnus", age=34, email="chess@magnusisgoat.com", cgpa = 9.41)
# print(student)
# print(dict(student))
print(student.model_dump_json())