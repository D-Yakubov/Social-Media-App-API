from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/get_post")
def get_post():
    return {"Name": "John Doe", "Age": 25, "Occupation": "Software Engineer"}

@app.post("/createposts")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']}, content: {payLoad['content']}"}