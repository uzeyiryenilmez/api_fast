from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import json

app = FastAPI()

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

with open('people.json', 'r') as f:
    people = json.load(f)['people']

print(people)

