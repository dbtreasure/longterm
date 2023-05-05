from fastapi import FastAPI, HTTPException, Request, Form, Body
from pydantic import BaseModel
from typing import Annotated
from operator import itemgetter
from models.client import Client
from supabase.client import add_client_from_signup, unsubscribe_client
import json

app = FastAPI()

class MandrillEvent(BaseModel):
    type: str
    fired_at: str
    data: dict

@app.post("/webhook/new_subscriber")
async def handle_webhook(
    type: str = Form(...),
    fired_at: str = Form(...),
    data_email: str = Form(..., alias="data[email]"),
    f_name: str = Form(..., alias="data[merges][FNAME]"),
    l_name: str = Form(..., alias="data[merges][LNAME]"),
):
    
    if type == "subscribe":
        await add_client_from_signup(Client(
            name=f"{f_name} {l_name}",
            email=data_email,
            account_status="signup"
        ))
    elif type == "unsubscribe":
        await unsubscribe_client(Client(
            email=data_email,
        ))
    return {"success": True}

@app.get("/webhook/new_subscriber")
async def handle_webhook():
    try:
        return {"success": True}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
