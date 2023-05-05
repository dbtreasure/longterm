# database_config.py

import requests
from models.client import Client
import os

# define a function that can send a POST to the supabase /clients table
async def add_client_from_signup(client: Client):
    # try catch block to handle errors
    try:
        # import SUPABASE_LONGTERM_API_KEY from os environment variables
        # supabase_key = os.environ.get("SUPABASE_BEARER_TKN_MAY_14")
        supabas_anon_key = os.environ.get("SUPABASE_LONGTERM_ANON_KEY")

        supabase_ref = "xizbdysxawruaeujhfpt"
        supabase_rest_url = f"https://{supabase_ref}.supabase.co/rest/v1"

        print(f"Adding client \
            name: {client.name} \
            email: {client.email} \
            status: {client.account_status} to database...")
        response = requests.post(
            f"{supabase_rest_url}/clients",
            headers={
                "apikey": supabas_anon_key,
                "Authorization": f"Bearer {supabas_anon_key}",
                "Content-Type": "application/json",
            },
            json={
                "name": client.name,
                "email": client.email,
                "account_status": client.account_status
            }
        )
        print('Client added to database!')
    except Exception as e:
        print(f"Error: {e}")