# This file is currently not being used for anything.

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json

app = FastAPI()

class Player(BaseModel):
    position: str
    nameParsed: str
    score4: str
    today: str
    thru: str
    score7: str
    score8: str
    score9: str
    score10: str
    total: str

class Config:
    schema_extra = {
        "example": {
            "position": "T1",
            "nameParsed": "C. Bezuidenhout",
            "score4": "-8",
            "today": "-4",
            "thru": "14",
            "score7": "68",
            "score8": "--",
            "score9": "--",
            "score10": "--",
            "total": "68"
        }
    }



@app.post("/players/")
async def create_player(player: Player):
    # player.nameParsed.
    return player

@app.get("/")
async def root():
    with open('sample.json') as f:
        data = json.load(f)
    return {"data": data}
