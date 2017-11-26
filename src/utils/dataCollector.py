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
    damageStats = {'BRONZE': [], 'SILVER': [], 'GOLD': [], 'PLATINUM': [], 'DIAMOND': [], 'UNRANKED': []}
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
                if tier == 'BRONZE':
                    if(supportBoolean == False):
                        stats['BRONZE']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                        damageStats['BRONZE'].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats['BRONZE']['AMOUNT'] += 1
                elif tier == 'SILVER':
                    if (supportBoolean == False):
                        stats['SILVER']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                        damageStats['SILVER'].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats['SILVER']['AMOUNT'] += 1
                elif tier == 'GOLD':
                    if (supportBoolean == False):
                        stats['GOLD']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                        damageStats['GOLD'].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats['GOLD']['AMOUNT'] += 1
                elif tier == 'PLATINUM':
                    if (supportBoolean == False):
                        stats['PLATINUM']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                        damageStats['PLATINUM'].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats['PLATINUM']['AMOUNT'] += 1
                elif tier == 'DIAMOND':
                    if (supportBoolean == False):
                        stats['DIAMOND']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                        damageStats['DIAMOND'].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats['DIAMOND']['AMOUNT'] += 1
                elif tier == 'UNRANKED':
                    if (supportBoolean == False):
                        stats['UNRANKED']['CS'].append(utils.get_player_stats(player, stat='totalMinionsKilled'))
                        damageStats['UNRANKED'].append(utils.get_player_stats(player, stat='totalDamageDealtToChampions'))
                    stats['UNRANKED']['AMOUNT'] += 1
                supportBoolean = False



    testPlayer = utils.get_participants(0,1)
    #print(testPlayer.get('totalDamageDealtToChampions'))
    #print(utils.get_player_stats(testPlayer,stat='totalDamageDealtToChampions'))

    bronzecs = pd.Series(stats['BRONZE']['CS'])
    silvercs = pd.Series(stats['SILVER']['CS'])
    goldcs = pd.Series(stats['GOLD']['CS'])
    platinumcs = pd.Series(stats['PLATINUM']['CS'])
    diamondcs = pd.Series(stats['DIAMOND']['CS'])
    unrankedcs = pd.Series(stats['UNRANKED']['CS'])

    bronzedmg = pd.Series(damageStats['BRONZE'])
    silverdmg = pd.Series(damageStats['SILVER'])
    golddmg = pd.Series(damageStats['GOLD'])
    platinumcdmg = pd.Series(damageStats['PLATINUM'])
    diamonddmg = pd.Series(damageStats['DIAMOND'])
    unrankeddmg = pd.Series(damageStats['UNRANKED'])

    # These are the CS average
    pp.pprint(bronzecs.mean())
    pp.pprint(silvercs.mean())
    pp.pprint(goldcs.mean())
    pp.pprint(platinumcs.mean())
    pp.pprint(diamondcs.mean())
    pp.pprint(unrankedcs.mean())

    print()

    # These are the damage averages
    pp.pprint(bronzedmg.mean())
    pp.pprint(silverdmg.mean())
    pp.pprint(golddmg.mean())
    pp.pprint(platinumcdmg.mean())
    pp.pprint(diamonddmg.mean())
    pp.pprint(unrankeddmg.mean())

    # These are the distributions
    print()
    print(stats['BRONZE']['AMOUNT'])
    print(stats['SILVER']['AMOUNT'])
    print(stats['GOLD']['AMOUNT'])
    print(stats['PLATINUM']['AMOUNT'])
    print(stats['DIAMOND']['AMOUNT'])
    print(stats['UNRANKED']['AMOUNT'])
if __name__ == '__main__':
    main()