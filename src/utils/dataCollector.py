# League Python data collector created by Danny Nguyen
import json, requests
import pprint  
import pandas as pd 
import numpy as np
from dataUtils import dataUtils

def main():
    files = ['matches1.json', 'matches2.json', 'matches3.json', 'matches4.json', 'matches5.json',
             'matches6.json', 'matches7.json', 'matches8.json', 'matches9.json', 'matches10.json']
    stats = {'BRONZE': {'CS':[], 'AMOUNT': 0}, 'SILVER': {'CS':[], 'AMOUNT': 0}, 'GOLD': {'CS':[], 'AMOUNT': 0},
             'PLATINUM': {'CS':[], 'AMOUNT': 0}, 'DIAMOND': {'CS':[], 'AMOUNT': 0}, 'UNRANKED': {'CS':[], 'AMOUNT': 0}}
    pp = pprint.PrettyPrinter()

    for file in files:
        utils = dataUtils(file)
        for matchID in range(0, 99): # For each match 
            for playerID in range(1, 10): # For each player in the match
                player = utils.get_participants(matchID, playerID)
                tier = player.get('highestAchievedSeasonTier')
                if tier == 'BRONZE':
                    stats['BRONZE']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    stats['BRONZE']['AMOUNT'] += 1
                elif tier == 'SILVER':
                    stats['SILVER']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    stats['SILVER']['AMOUNT'] += 1
                elif tier == 'GOLD':
                    stats['GOLD']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    stats['GOLD']['AMOUNT'] += 1
                elif tier == 'PLATINUM':
                    stats['PLATINUM']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    stats['PLATINUM']['AMOUNT'] += 1
                elif tier == 'DIAMOND':
                    stats['DIAMOND']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    stats['DIAMOND']['AMOUNT'] += 1
                elif tier == 'UNRANKED':
                    stats['UNRANKED']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    stats['UNRANKED']['AMOUNT'] += 1


    bronzecs = pd.Series(stats['BRONZE']['CS'])
    silvercs = pd.Series(stats['SILVER']['CS'])
    goldcs = pd.Series(stats['GOLD']['CS'])
    platinumcs = pd.Series(stats['PLATINUM']['CS'])
    diamondcs = pd.Series(stats['DIAMOND']['CS'])
    unrankedcs = pd.Series(stats['UNRANKED']['CS'])

    # These are the CS average
    pp.pprint(bronzecs.mean())
    pp.pprint(silvercs.mean())
    pp.pprint(goldcs.mean())
    pp.pprint(platinumcs.mean())
    pp.pprint(diamondcs.mean())
    pp.pprint(unrankedcs.mean())

    # These are the distributions
    print(stats['BRONZE']['AMOUNT'])
    print(stats['SILVER']['AMOUNT'])
    print(stats['GOLD']['AMOUNT'])
    print(stats['PLATINUM']['AMOUNT'])
    print(stats['DIAMOND']['AMOUNT'])
    print(stats['UNRANKED']['AMOUNT'])
if __name__ == '__main__':
    main()