import plaid
from plaid.api import plaid_api
import streamlit as st

def create_plaid_client():
    configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': st.secrets['plaid']['client_id'],
            'secret': st.secrets['plaid']['secret']
        }
    )
    return plaid_api.PlaidApi(plaid.ApiClient(configuration))

def create_link_token(client):
    return client.link_token_create({
        'user': {'client_user_id': 'debt-simulator-user'},
        'products': ['auth', 'transactions'],
        'client_name': "Debt Destroyer",
        'country_codes': ['US', 'CA', 'EU'],
        'language': 'en'
    })