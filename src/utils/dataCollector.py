# League Python data collector created by Danny Nguyen
import json, requests
import pprint  
import pandas as pd 
from dataUtils import dataUtils

def main():
    utils = dataUtils('matches1.json')
    averCS = []
    for players in utils.get_participants(1):
        stats = utils.get_player_stats(players)
        averCS.append(stats.get('totalMinionsKilled'))
    



if __name__ == '__main__':
    main()

"""   Commented out code since we might not need it for analysis
# # # # # # # # # # # # # # # # # # # # # # # # # #
# Get information about a certain summoner
#
# Params: 
#   Name - Name of the summoner
# Returns:
#   Dictionary of the data read from Riot's API.
def get_summoner(name):
    settings = {}
    with open('riot-api-key.txt') as key:
        for line in key: # Grab the api key from a file. 
            if len(line) != 0:
                settings['riot_key'] = line 

    settings['summoner-name'] = name # Put summoner name here if you have one
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + settings['summoner-name'] + '?api_key=' + settings['riot_key'];

    try:
        r = requests.get(url)
        data = json.loads(r.text)
        return data
    except Exception as e:
        print("Unable to read json data. ", e)
"""

