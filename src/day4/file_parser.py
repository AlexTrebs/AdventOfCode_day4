import sys

def getInputFile(fileName):
    file = "./docs/" + fileName

    with open(file,'r') as i:
            lines = i.readlines()
    return lines

def parseWinningAndDrawn(game):

    return (list(map(int,g.strip().split())) for g in game.split("|"))

def parseGames(line):

    tempList = line.split(":")
    
    gameNum = tempList[0].strip().strip("Card ")
    winningNumbers, drawnNumbers = parseWinningAndDrawn(tempList[1])
    
    return {gameNum: {"Winners":winningNumbers,"Drawn":drawnNumbers}}

def parseFile(fileName):
    inputLines = getInputFile(fileName)

    gameDict = {}

    for line in inputLines:
        gameDict.update(parseGames(line))

    return gameDict

if __name__ == "__main__":
    parseFile()