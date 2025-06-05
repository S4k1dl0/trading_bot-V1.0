import requests
import os

def send_discord(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    payload = {"content": message}
    requests.post(webhook_url, json=payload)
