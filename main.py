import requests, pyperclip, sys

next_page_cursor = ""
data = []

while True:
    game_id = input("game_id: ")
    if game_id.isdigit():
        break
    else:
        print("please enter a valid game id.")
        continue

while True:
    server_json = requests.get(f"https://games.roblox.com/v1/games/{game_id}/servers/Public?sortOrder=Asc&limit=100&cursor={next_page_cursor}").json()
    print(f"next_page_cursor: {next_page_cursor}")
    if "data" in server_json:
        for server_json_data in server_json["data"]:
            if "ping" in server_json_data:
                data.append({"id": server_json_data["id"], "ping": server_json_data["ping"]})
    if "nextPageCursor" in server_json:
        if server_json["nextPageCursor"] is None:
            break
        else:
            next_page_cursor = server_json["nextPageCursor"]

try:
    min_ping = min(data, key = lambda x: x["ping"])
    pyperclip.copy(f"Roblox.GameLauncher.joinGameInstance({game_id}, '{min_ping['id']}') // Ping: {min_ping['ping']}")
except ValueError:
    print("could not find server")
    input("press any key to exit")
