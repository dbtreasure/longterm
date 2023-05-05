# database_config.py

import requests
from models.client import Client
import os

# import SUPABASE_LONGTERM_API_KEY from os environment variables
supabase_key = os.environ.get("SUPABASE_LONGTERM_API_KEY")

supabase_ref = "xizbdysxawruaeujhfpt"
supabase_rest_url = f"https://{supabase_ref}.supabase.co/rest/v1"

# define a function that can send a POST to the supabase /clients table
async def add_client_from_signup(Client):
    # try catch block to handle errors
    try:
        print(f"Adding client {Client.name} to database...")
        response = requests.post(
            f"{supabase_rest_url}/clients",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {supabase_key}",
            },
            data={
                name: Client.name,
                email: Client.email,
                account_status: "signup"
            }
        )
        print('Client added to database!')
        print(response.json())
    
    except Exception as e:
        print(f"Error: {e}")