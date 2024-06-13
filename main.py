from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import json
import models
import submissions
from database import *
from generator import passGenerator, addNumbers, toUpper
from fastapi.responses import HTMLResponse
from schemas import Item

app = FastAPI()
app.include_router(submissions.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/seed")
async def seed(db: Session = Depends(get_db)):
    if db.query(models.LeakedPassword).all() == []:
        with open("./data/leaked.json", "r") as json_file: 
            data = json.load(json_file)
            for row in data:
                password = models.LeakedPassword(content=row["content"])
                db.add(password)
        db.commit()
    if db.query(models.GeneratedPassword).all() == []:
        with open("./data/generated.json", "r") as json_file: 
            data = json.load(json_file)
            for row in data:
                password = models.GeneratedPassword(content=row["content"])
                db.add(password)
        db.commit()

    return {"message": "Hello World"}



@app.post("/generator/")
async def submit_data(item: Item):
    passphrase = passGenerator(int(item.value))
    passphrase = addNumbers(int(item.number), passphrase)
    
    return {"phrase_value": passphrase}

@app.post("/uppercase/")
async def submit_data(item: Item):
    passphrase = toUpper(item.value)    
    return {"phrase_value": passphrase}

app.mount("/", StaticFiles(directory="static", html = True), name="static")

