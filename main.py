from model import summary_pipline
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile

app = FastAPI()

class TextIn(BaseModel):
    ARTICLE: str

@app.get("/")
def read_root():
    return {"Hello": "Claris"}
 
@app.post("/summary")
def summary(payload: TextIn):
    return summary_pipline(payload.ARTICLE)
