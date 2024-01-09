import sys
import file_parser

def getNumberOfWinners(winners, drawn):
    return sum([drawn.count(winningNum) for winningNum in winners])
    
def getScore(numberOfwinners):    
    return 2**(numberOfwinners-1)

def getWinnings(winners, drawn):
    numberOfWinners = getNumberOfWinners(winners, drawn)
    
    if(numberOfWinners == 0):
        
        return 0
    
    else:
        
        return getScore(numberOfWinners)

if __name__ == "__main__":    
    print(getWinnings(tuple(sys.argv[1:])))