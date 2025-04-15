import json
import psutil
import os

def load_games(filename="games.json"):
    if not os.path.exists(filename):
        print("Konfogurationsdatei nicht gefunden!")
        return{}, []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        games = data.get("games", {})
        blacklist = data.get("blacklist", [])
        return games, blacklist

def detect_running_games(games, blacklist):
    #scann all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # name of the running program
            name = proc.info['name']
            if name:
                lname = name.lower()
                if lname in blacklist:
                    continue
                #game from list found
                if lname in games:
                    return games[lname]
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Some processes are not for watching
            continue

    return None #nothing found



if __name__ == "__main__":
    games, blacklist = load_games()
    current_game = detect_running_games(games, blacklist)
    if current_game:
        print(f"🎮 Aktives Spiel erkannt: {current_game}")
    else:
        print("🔍 Kein bekanntes Spiel erkannt oder nur geblacklistete Prozesse aktiv.")
