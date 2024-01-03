from model import summary_pipline, question_anwser
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile

app = FastAPI()

class ArticleIn(BaseModel):
    ARTICLE: str

class QAIn(BaseModel):
    question: str
    context: str

@app.get("/")
def read_root():
    return {"Hello": "Claris"}
 
@app.post("/summary")
def summary(payload: ArticleIn):
    return summary_pipline(payload.ARTICLE)

@app.post("/questionanswer")
def answer(payload: QAIn):
    return question_anwser(payload.question, payload.context)
