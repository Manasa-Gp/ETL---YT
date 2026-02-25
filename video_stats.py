import requests
import json
from datetime import date

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv('API_KEY')
CHANNEL_HANDLE = 'BTS'

try:
    def get_playlist_id():
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        #print(response)

        data = response.json()

        #print(json.dumps(data,indent = 4))

        channel_items = data['items'][0]

        channel_playlistid = channel_items['contentDetails']['relatedPlaylists']['uploads']

        return channel_playlistid

except requests.exceptions.RequestException as e:
    raise e


if __name__ == "__main__":
    print("executed")
    get_playlist_id()
else:
    print("not executed")