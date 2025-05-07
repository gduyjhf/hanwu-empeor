from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from liuche_bot import emperor_liuche

app = FastAPI()

class Question(BaseModel):
    prompt: str

@app.post("/ask")
def ask_emperor(question: Question):
    try:
        answer = emperor_liuche(question.prompt)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.mount("/", StaticFiles(directory="static", html=True), name="static")
