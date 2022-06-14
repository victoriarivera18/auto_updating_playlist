#1: Access user playlists and saved (liked) songs
#2: Get list of all the tracks (by name or ID) in the saved songs
#3: For every song
#       - check language
#        - if spanish: 
#                - check if is already in spanish playlist
#                       - if no: add to playlist

#                       -else: skip

#        - else: skip do nothing
#       
#

#4: improvement: only check the latest 20-25 songs added 

import json
import urllib3
import base64
import requests
import sys

from secrets import spotify_user_id, client_id, client_secret



def auth(): 
    client_cred_b64 = base64.b64encode(bytes(client_id + ":" + client_secret, "ISO-8859-1")).decode("ascii")
    method = "POST"

    url = "https://accounts.spotify.com/api/token"
    
    data = {
        "grant_type" : "client_credentials"
    }

    headers = {
        "Authorization" : f"Basic {client_cred_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_response = requests.post(url, data=data, headers=headers)
    token_data = token_response.json()




if __name__ == "__main__":
    #start program
    auth()

    #set variables

















# query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id) # using secrets information
#   response = requests.get(query, data=None, headers={ # from api documentation
#       "Accept": "application/json",
#       "Content-Type": "application/json",
#       "Authorization": "Bearer {}".format(spotify_token)
#   })

#  response_json = response.json() #playlists name info