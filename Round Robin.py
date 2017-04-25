import json

######
#
# Functions take 'n' number of players, divides them into groups of 4 or 6 depending on which decode
# function is called, and then sorts the players into matches as per Andy's round robin spreadsheet
#
# Andy informed we don't yet need to worry about numbers of players that don't evenly divide
# into appropriate groups
#
# returns DICT of rounds
#####



def fourDoubles(player1 , player2, player3, player4):
    """Takes a pool of 4 players rounds with doubles matchups"""

    # As there are only 6 possible team combinations I have simply manually entered the games
    # and returned them as a list, where each sublist is a match and each sub-sublist is a team

    teams = [player1, player2], [player1, player3], [player1, player4], [player2, player3], [player2, player4], [player3, player4]
    games = []
    games += [teams[0],teams[5]],[teams[1],teams[4]],[teams[2],teams[3]]
    return games

def fourDoublesSingles(player1 , player2, player3, player4):
    """Takes a pool of 4 players rounds with doubles and singles matchups"""
    # resuses the code in the above function but adds all 6 possible games

    pool = (player1, player2, player3, player4)
    teams = [player1, player2], [player1, player3], [player1, player4], [player2, player3], [player2, player4], [player3, player4]
    games = []
    games += [teams[0],teams[5]],[teams[1],teams[4]],[teams[2],teams[3]]
    i = 0
    for match in teams:
        games += [[teams[i][0],teams[i][1]]]
        i+=1
    return games

def sixDoublesSingles(player1 , player2, player3, player4, player5, player6):
    """Takes a pool of 6 players rounds with doubles and singles matchups"""

    # As there are only 6 games, manually code them (singles and doubles) as per the spreadsheet

    pool = (player1, player2, player3, player4, player5, player6)
    teams = [player3, player4], [player1, player5], [player1, player4], [player5, player6], [player2, player6], [player2, player3]
    games = []
    games += [teams[0],teams[3]],[teams[1],teams[4]],[teams[2],teams[5]]
    games += [pool[0],pool[1]],[pool[2], pool[3]],[pool[4], pool[5]]
    return games



def fourDoublesReturn(pool):
    """Takes a pool of n (where n % 4 == 0) players as DICT and returns DICT 'rounds' with doubles matchups"""
    # used to decode JSON then call fourDoubles method
    i = 0
    x = int(((len(pool['players'])) / 4)) ### can work with any number of players where n%4=0
    matchUp = []
    for y in range(x):
        matchUp += fourDoubles((pool['players'][i]), (pool['players'][i + 1]), (pool['players'][i + 2]),
                               (pool['players'][i + 3]))
        i += 4
    return {'rounds': matchUp}

def fourSinglesReturn(pool):
    """Takes a pool of n (where n % 4 == 0) players as DICT and returns DICT 'rounds' with singles matchups"""
    #used to decode JSON then call fourDoublesSingles method
    i = 0
    x = int(((len(pool['players'])) / 4)) ### can work with any number of players where n%4=0
    matchUp = []
    for y in range(x):
        matchUp += fourDoublesSingles((pool['players'][i]), (pool['players'][i + 1]), (pool['players'][i + 2]),
                               (pool['players'][i + 3]))
        i += 4
    return {'rounds': matchUp}

def sixSinglesReturn(pool):
    """Takes a pool of n (where n % 6 == 0) players as DICT and returns DICT 'rounds' with singles matchups"""
    #used to decode JSON then call sixDoublesSingles method
    i = 0
    x = int(((len(pool['players'])) / 6)) ### can work with any number of players where n%6=0
    matchUp = []
    for y in range(x):
        matchUp += sixDoublesSingles((pool['players'][i]), (pool['players'][i + 1]), (pool['players'][i + 2]),
                               (pool['players'][i + 3]), (pool['players'][i + 4]), (pool['players'][i + 5]))
        i += 6
    return {'rounds': matchUp}

testCase = {"compName":"Thursday Night Singles","singlesDoubles":"singles","type":"poolDraws","players": ["Roger Federer","Andre Agassi","Andy Murray","Serena Williams","a","b","c","d","e","f","g","h"]}  ###test DICT 8 players
testCase2 = {"compName":"Thursday Night Singles","singlesDoubles":"singles","type":"poolDraws","players": ["Roger Federer","Andre Agassi","Andy Murray","Serena Williams","Tom Hill","Jack Jensen","a","b","c","d","e","f"]} ###test DICT 12 players
print(fourDoublesReturn(testCase))
print(fourSinglesReturn(testCase))
print(sixSinglesReturn(testCase2))
