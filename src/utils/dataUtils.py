import json
import pandas as pd

"""
    dataUtils will contain all of the functions needed for grabbing certain data from
    the file provided.

    This is for data science project only. - Created by Danny Nguyen
"""
class dataUtils:
    
    def __init__(self, fileName):
        self.name = fileName
        with open('../data/' + self.name) as file:
            data = pd.read_json(file)
            self.allMatches = data.get('matches')

    """
        Return the entire data array for the file
    """
    def get_all_matches(self):
        return self.allMatches
        
    """
        Return the match information for the matchID for the file.
        If the id is out of range, return nothing.
    """
    def get_match(self, matchID):
        if matchID < -1 or matchID > 99:
            return None
        return self.allMatches.get(matchID)

    """
        Return all of the players of a given match 
        if player ID is given, return the stats for that ID
    """
    def get_participants(self, matchID, playerId=-1):
        if matchID < -1 or matchID > 99:
            return None
        match = self.get_match(matchID)
        
        if playerId != -1: # If given player ID of a match is given, return that player stats
            participants = match.get('participants')
            return participants[playerId]
    
        return match.get('participants')

    """
        Get all of the player stats for the match. 
        If stat is defined, then return the specific stat for that game. 
    """
    def get_player_stats(self, player, stat=''):
        if stat != '':
            playerStats = player.get('stats')
            return playerStats.get(stat)
        return player.get('stats')

    """
        Get all of the player timeline for the match.
        if Stat is defined, then return the specific timeline for that game
    """
    def get_player_timeline(self, player, stat='')
    if stat != '':
        playerStats = player.get('timeline')
        return playerStats.get(stat)
    return player.get('timeline')