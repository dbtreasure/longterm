# client.py

# Path: models/client.py

from pydantic import BaseModel

class Client(BaseModel):
    name: str
    email: str
    phone: str = None
    goal: str = None
    notes: str = None
    account_status: str = None