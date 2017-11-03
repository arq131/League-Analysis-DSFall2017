# League Python data collector
import json, requests

def main():
    settings = {}
    with open('riot-api-key.txt') as key:
        for line in key: # Grab the api key from a file. 
            if len(line) != 0:
                settings['riot_key'] = line 

    settings['summoner-name'] = 'Skirex' # Put summoner name here if you have one
    settings['region'] = 'name'
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + settings['summoner-name'] + '?api_key=' + settings['riot_key'];

    try:
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)
    except Exception as e:
        print("Unable to read json data. ", e)


if __name__ == '__main__':
    main()