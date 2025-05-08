from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class AddInput(BaseModel):
  a: int
  b: int

@app.get('/tools')
def list_tools():
  return {
    'tools': [
      {
        'name': 'add_numbers',
        'description': 'Add two numbers together',
        'input_schema': {
          'a': 'int',
          'b': 'int'
        }
      }
    ]
  }

@app.post('/tools/add_numbers/call')
def call_add_numbers(data: AddInput):
  return {
    'result': data.a + data.b
  }