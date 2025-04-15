import psutil

known_games = {
    "hades.exe": "Hades",
    "eldenring.exe": "Elden Ring",
    "slaythespire.exe": "Slay the Spire",
    "vampiresurvivors.exe": "Vampire Survivors",
    "streamavatars.exe": "Stream Avatars",
}

def detect_running_games():
    #scann all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # name of the running program
            name = proc.info['name']
            if name and name.lower() in known_games:
                #game from list found
                return known_games[name.lower()]
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Some processes are not for watching
            continue
    return None #no games found

################## This is only for checking if psutil works and will be removed in one of the next itterations
def list_running_executables():
    print("Starte Prozess-Scan...\n")

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # name of the running program
            name = proc.info['name']
            if name and name.endswith('.exe'):
                print(f"PID: {proc.info['pid']} | Name: {name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Some processes are not for watching
            continue
#################          
          
if __name__ == "__main__":
    current_game = detect_running_games()
    if current_game:
        print(f"Aktives Spiel erkannt: {current_game})")
    else:
        print("Kein bekanntes Spiel gefunden.")
