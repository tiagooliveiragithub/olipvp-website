import requests
from django.conf import settings
from django.http import JsonResponse
from mcrcon import MCRcon
import re

def rcon_command(username, plan):
        with MCRcon(settings.MINECRAFT_IP, settings.RCON_PASSWORD) as client:
            # response = client.run(f"lp user {username} permission set lunatic true")
            response = client.command(f"say user {username} permission set {plan} true")

def server_info():
    data = {
        "status" : True,
        "version": "1.19.4",
        "IP": settings.MINECRAFT_IP + ":" + settings.MINECRAFT_PORT,
        "name": settings.APP_NAME,
    }
    
    try:
        with MCRcon(settings.MINECRAFT_IP, settings.RCON_PASSWORD) as client:
            raw_players = client.command("list")
            color_removed = remove_color_codes(raw_players)
            players = extract_first_two_numbers(color_removed)
            data["players"] = players
            return data
    except Exception as e:
        print(e)
        data["status"] = False
        return data

def remove_color_codes(text):
    # This regex finds '§' followed by any character
    return re.sub(r"§.", "", text)

def extract_first_two_numbers(text):
    # Find all occurrences of numbers in the text
    numbers = re.findall(r"\d+", text)
    # Check if there are at least two numbers found
    if len(numbers) >= 2:
        # Return the first two numbers joined by a "/"
        return f"{numbers[0]}/{numbers[1]}"