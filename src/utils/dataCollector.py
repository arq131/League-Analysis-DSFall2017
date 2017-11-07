# League Python data collector created by Danny Nguyen
import json, requests

def main():
    get_all_matches('matches1.json')
    
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

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Get all of the matches from a locally stored file.
#
# Params: 
#   filename - The name of the file to get the data from
# Returns:
#   Dictionary of all of the matches in the provided file.
def get_all_matches(filename):
    with open('../data/' + filename) as file:
        data = json.load(file)
        return data

if __name__ == '__main__':
    main()