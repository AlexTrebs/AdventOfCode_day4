from file_parser import parseFile
from calculate_winnings import getWinnings
from consts.filenames import getFileName
import sys

def calulateExtraCards(scratchCards):
    winningCards = sum(getWinnings(*tuple(i.values())) for i in scratchCards)


def calculateTotalWinnings(scratchCards, amountOfNewScratchCards, winnings):
    totalWon = 1
    print(len(scratchCards))
    if amountOfNewScratchCards == 0 or len(winnings) == 1:
        return totalWon
    
    for idx, i in enumerate(winnings[:amountOfNewScratchCards]):
        if i < len(scratchCards):
            totalWon += calculateTotalWinnings(scratchCards[idx+1::], i, winnings[idx+1::])
        elif i > 0:
            totalWon += calculateTotalWinnings(scratchCards[idx+1::], len(scratchCards)-1, winnings[idx+1::])
        
    return totalWon  

def getTotalWinnings(filename):
    scratchCards = parseFile(filename)
    winnings = list(getWinnings(*tuple(i.values())) for i in parseFile(filename).values())
    amountOfScratchCards = len(scratchCards)

    print(calculateTotalWinnings(list(scratchCards.values()),amountOfScratchCards,winnings))

if __name__ == "__main__":
    print(getTotalWinnings(getFileName(sys.argv[1:][0])))