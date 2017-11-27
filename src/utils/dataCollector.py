# League Python data collector created by Danny Nguyen
import json, requests
import pprint
import pandas as pd
import numpy as np
from dataUtils import dataUtils
import matplotlib.pyplot as plt


def prettyP(rank, stat):
    print('{}:\n\tMean: {}\n\tMedian: {}\n\tStd. Dev: {}\n\tMin: {}\n\tMax: {}'.format(rank, round(stat.mean(), 2),
                                                                                       round(stat.median(), 2),
                                                                                       round(stat.std(), 2),
                                                                                       round(stat.min(), 2),
                                                                                       round(stat.max(), 2)))


def main():
    files = ['matches1.json', 'matches2.json', 'matches3.json', 'matches4.json', 'matches5.json',
             'matches6.json', 'matches7.json', 'matches8.json', 'matches9.json', 'matches10.json']

    ranks = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'UNRANKED']

    stats = {'BRONZE':   {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}},
             'SILVER':   {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}},
             'GOLD':     {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}},
             'PLATINUM': {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}},
             'DIAMOND':  {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}},
             'MASTER':   {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}},
             'UNRANKED': {'CS': [], 'AMOUNT': 0, 'KILLS': [], 'DEATHS': [], 'ASSISTS': [], 'GOLDEARNED': [], 'GOLDDELTA': {'0-10':[],'10-20':[],'30-end':[]}}
             }

    damageStats = {'BRONZE': [], 'SILVER': [], 'GOLD': [], 'PLATINUM': [], 'DIAMOND': [], 'MASTER': [], 'UNRANKED': []}

    pp = pprint.PrettyPrinter()

    for file in files:
        utils = dataUtils(file)
        for matchID in range(0, 100):  # For each match
            for playerID in range(0, 10):  # For each player in the match
                player = utils.get_participants(matchID, playerID)
                tier = player.get('highestAchievedSeasonTier')
                if utils.get_player_timeline(player, stat='role') != 'DUO_SUPPORT' \
                        and utils.get_player_timeline(player, stat='creepsPerMinDeltas') is not None \
                        and utils.get_player_stats(player, stat='totalDamageDealtToChampions') > 0:
                    stats[tier]['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                    damageStats[tier].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats[tier]['KILLS'].append(utils.get_player_stats(player, stat='kills'))
                    stats[tier]['DEATHS'].append(utils.get_player_stats(player, stat='deaths'))
                    stats[tier]['ASSISTS'].append(utils.get_player_stats(player, stat='assists'))
                    stats[tier]['GOLDEARNED'].append(utils.get_player_stats(player, stat='goldEarned'))
                    #print(player)
                    stats[tier]['GOLDDELTA']['0-10'].append(
                        utils.get_player_timeline(player, stat='goldPerMinDeltas').get('0-10'))
                    if utils.get_player_timeline(player, stat='goldPerMinDeltas').get('10-20') is not None:
                        stats[tier]['GOLDDELTA']['10-20'].append(
                            utils.get_player_timeline(player, stat='goldPerMinDeltas').get('10-20'))
                    if utils.get_player_timeline(player, stat='goldPerMinDeltas').get('30-end') is not None:
                        stats[tier]['GOLDDELTA']['30-end'].append(
                            utils.get_player_timeline(player, stat='goldPerMinDeltas').get('30-end'))

                stats[tier]['AMOUNT'] += 1

    player = utils.get_participants(1, 1)
    #print(utils.get_player_timeline(player, stat='goldPerMinDeltas').get('0-10'))
    #print(utils.get_player_timeline(player, stat='goldPerMinDeltas').get('10-20'))
    #print(utils.get_player_timeline(player, stat='goldPerMinDeltas').get('30-end'))

    print('Distribution')
    total = 0;
    for rank in ranks:
        percent = stats[rank]['AMOUNT'] / 10000.0
        print('{}: {} ({}%)'.format(rank, stats[rank]['AMOUNT'], round(percent * 100, 5)))
        total += stats[rank]['AMOUNT']
    print(total)
    x = 1
    print('Damage done to champions by Rank')
    for rank in ranks:
        dmg = pd.Series(damageStats[rank])
        prettyP(rank, dmg)
        plt.subplot(4, 2, x)
        plt.hist(dmg, alpha=0.2, label=rank)
        plt.legend(loc='upper right')
        x += 1

    #plt.show()
    
    print('Creep Scores')
    for rank in ranks:
        cs = pd.Series(stats[rank]['CS'])
        prettyP(rank, cs)

    print('Gold Earned')
    for rank in ranks:
        gold = pd.Series(stats[rank]['GOLDEARNED'])
        prettyP(rank, gold)

    print('Gold Deltas')
    for rank in ranks:
        goldDelta1 = pd.Series(stats[rank]['GOLDDELTA']['0-10'])
        goldDelta2 = pd.Series(stats[rank]['GOLDDELTA']['10-20'])
        goldDelta3 = pd.Series(stats[rank]['GOLDDELTA']['30-end'])
        prettyP(rank, goldDelta1)
        prettyP(rank, goldDelta2)
        prettyP(rank, goldDelta3)

    
    print('K/D/A')
    for rank in ranks:
        k = pd.Series(stats[rank]['KILLS'])
        d = pd.Series(stats[rank]['DEATHS'])
        a = pd.Series(stats[rank]['ASSISTS'])
        print('{}:\n\tMean: {}/{}/{}\n\tMedian: {}/{}/{}\n\tStd. Dev: {}/{}/{}\n\tMin: {}/{}/{}\n\tMax: {}/{}/{}'.format(
                rank, round(k.mean(), 2), round(d.mean(), 2), round(a.mean(), 2), 
                      round(k.median(), 2), round(d.median(), 2), round(a.median(), 2),
                      round(k.std(), 2), round(d.std(), 2), round(a.median(), 2),
                      round(k.min(), 2), round(d.min(), 2), round(a.min(), 2),
                      round(k.max(), 2), round(k.max(), 2), round (a.max(), 2)))
    


if __name__ == '__main__':
    main()
