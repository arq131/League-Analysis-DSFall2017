# League Python data collector created by Danny Nguyen
import json, requests
import pprint  
import pandas as pd 
import numpy as np
from dataUtils import dataUtils

def prettyP(rank, stat):
    print('{}:\n\tMean: {}\n\tMedian: {}\n\tStd. Dev: {}\n\tMin: {}\n\tMax: {}'.format(rank, round(stat.mean(), 2), round(stat.median(), 2), 
            round(stat.std(), 2), round(stat.min(), 2), round(stat.max(), 2)))

def main():
    files = ['matches1.json', 'matches2.json', 'matches3.json', 'matches4.json', 'matches5.json',
             'matches6.json', 'matches7.json', 'matches8.json', 'matches9.json', 'matches10.json']

    ranks = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'UNRANKED']

    stats = {'BRONZE': {'CS':[], 'AMOUNT': 0}, 'SILVER': {'CS':[], 'AMOUNT': 0}, 'GOLD': {'CS':[], 'AMOUNT': 0},
             'PLATINUM': {'CS':[], 'AMOUNT': 0}, 'DIAMOND': {'CS':[], 'AMOUNT': 0}, 'MASTER': {'CS':[], 'AMOUNT': 0},
             'UNRANKED': {'CS':[], 'AMOUNT': 0} }
    
    damageStats = {'BRONZE': [], 'SILVER': [], 'GOLD': [], 'PLATINUM': [], 'DIAMOND': [], 'MASTER': [], 'UNRANKED': []}
    
    supportId = [12, 432, 53, 201, 40, 43, 89, 117, 25, 267, 497, 37, 16, 223, 44, 412, 26, 143]
    
    pp = pprint.PrettyPrinter()
    supportBoolean = False;

    for file in files:
        utils = dataUtils(file)
        for matchID in range(0, 99): # For each match 
            for playerID in range(1, 10): # For each player in the match
                player = utils.get_participants(matchID, playerID)
                if player.get('championId') in supportId:
                    supportBoolean = True;
                tier = player.get('highestAchievedSeasonTier')
                if (supportBoolean == False):
                    stats[tier]['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    damageStats[tier].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                stats[tier]['AMOUNT'] += 1
                supportBoolean = False

    print('Damage done to champions by Rank')
    for rank in ranks:
        dmg = pd.Series(damageStats[rank])
        prettyP(rank, dmg)

    print('Creep Scores')
    for rank in ranks:
        cs = pd.Series(stats[rank]['CS'])
        prettyP(rank, cs)

if __name__ == '__main__':
    main()

