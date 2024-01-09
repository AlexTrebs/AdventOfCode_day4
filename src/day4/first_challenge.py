from file_parser import parseFile
from calculate_winnings import getWinnings
from consts.filenames import getFileName
import sys

def calculateTotalWinnings(filename):
    return sum(getWinnings(*tuple(i.values())) for i in parseFile(filename).values())

if __name__ == "__main__":
    print(calculateTotalWinnings(getFileName(sys.argv[1:][0])))