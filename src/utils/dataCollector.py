# League Python data collector created by Danny Nguyen
import json, requests
import pprint  
import pandas as pd 
import numpy as np
from dataUtils import dataUtils
import matplotlib.pyplot as plt



def prettyP(rank, stat):
    print('{}:\n\tMean: {}\n\tMedian: {}\n\tStd. Dev: {}\n\tMin: {}\n\tMax: {}'.format(rank, round(stat.mean(), 2), round(stat.median(), 2), 
            round(stat.std(), 2), round(stat.min(), 2), round(stat.max(), 2)))

def main():
    files = ['matches1.json', 'matches2.json', 'matches3.json', 'matches4.json', 'matches5.json',
             'matches6.json', 'matches7.json', 'matches8.json', 'matches9.json', 'matches10.json']

    ranks = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'UNRANKED']

    stats = {'BRONZE':   {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []},
             'SILVER':   {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []},
             'GOLD':     {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []},
             'PLATINUM': {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []},
             'DIAMOND':  {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []},
             'MASTER':   {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []},
             'UNRANKED': {'CS':[], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': []}
            }
    
    damageStats = {'BRONZE': [], 'SILVER': [], 'GOLD': [], 'PLATINUM': [], 'DIAMOND': [], 'MASTER': [], 'UNRANKED': []}

    pp = pprint.PrettyPrinter()

    for file in files:
        utils = dataUtils(file)
        for matchID in range(0, 100): # For each match 
            for playerID in range(0, 10): # For each player in the match
                player = utils.get_participants(matchID, playerID)
                tier = player.get('highestAchievedSeasonTier')
                if utils.get_player_timeline(player, stat='role') != 'DUO_SUPPORT' \
                        and utils.get_player_stats(player, stat='totalDamageDealtToChampions') > 0:
                    stats[tier]['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    damageStats[tier].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats[tier]['KILLS'].append(utils.get_player_stats(player, stat='kills'))
                    stats[tier]['DEATHS'].append(utils.get_player_stats(player, stat='deaths'))
                    stats[tier]['ASSISTS'].append(utils.get_player_stats(player, stat='assists'))
                stats[tier]['AMOUNT'] += 1



    print('Distribution')
    total = 0;
    for rank in ranks:
        percent = stats[rank]['AMOUNT'] / 10000.0
        print('{}: {} ({}%)'.format(rank, stats[rank]['AMOUNT'], round(percent * 100, 5)))
        total += stats[rank]['AMOUNT']
    print(total)

    print('Damage done to champions by Rank')
    for rank in ranks:
        print(rank)
        dmg = pd.Series(damageStats[rank])
        prettyP(rank, dmg)
        plt.hist(dmg, alpha = 0.2, label=rank)
    plt.legend(loc='upper right')
    plt.show()


    print('Creep Scores')
    for rank in ranks:
        cs = pd.Series(stats[rank]['CS'])
        prettyP(rank, cs)

    ''' Work in progress
    print('K/D/A')
    for rank in ranks:
        k = pd.Series(stats[tier]['KILLS'])
        d = pd.Series(stats[tier]['DEATHS'])
        a = pd.Series(stats[tier]['ASSISTS'])
        prettyP(rank, k)
    '''

if __name__ == '__main__':
    main()

