import json

######
#
# Very basic first attempt, the two functions fourDoubles and fourDoublesSingles
# take 4 player names and sort them into matches as per Andy's spreadsheet
# I have not yet encoded the results as a JSON as I am not sure of the best way yet
#
# I can write additional code to break a list of players up into multiples of four and pass each one to
# one of these methods or we could do it a different way depending on how the info is passed
#
# I still have to write the 6 player method but will be the same as below
#
#####



def fourDoubles(player1 , player2, player3, player4):

    # As there are only 6 possible team combinations I have simply manually entered the games
    # and returned them as a list, where each sublist is a match and each sub-sublist is a team

    teams = [player1, player2], [player1, player3], [player1, player4], [player2, player3], [player2, player4], [player3, player4]
    games = []
    games += [teams[0],teams[5]],[teams[1],teams[4]],[teams[2],teams[3]]
    return games

def fourDoublesSingles(player1 , player2, player3, player4):

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

def fourDoublesReturn(jsonPool):

    # used to decode JSON then call fourDoubles method

    pool = json.loads(jsonPool)
    matchUp = fourDoubles((pool['players'][0]), (pool['players'][1]), (pool['players'][2]), (pool['players'][3]))
    return matchUp

def fourSinglesReturn(jsonPool):

    #used to decode JSON then call fourDoublesSingles method

    pool = json.loads(jsonPool)
    matchUp = fourDoublesSingles((pool['players'][0]), (pool['players'][1]), (pool['players'][2]), (pool['players'][3]))
    return matchUp

testCase = '{"players":["Pete","Andy","Jack","Tom"]}'  ###test JSON, not 100% sure if correct

print(fourDoublesReturn(testCase))
print(fourSinglesReturn(testCase))