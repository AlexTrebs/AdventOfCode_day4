import pytest
from src.day4.file_parser import parseWinningAndDrawn, parseGames

class TestFileParser():

    mockGame = "Game 1: 2 4 5 6 7 | 2 4 25 66 6252 2626262"
    mockWinners = [2,4,5,6,7]
    mockDrawn = [2,4,25,66,6252,2626262]
    mockGameSplit = {"Game 1":{"Winners":mockWinners, "Drawn":mockDrawn}}
    
    def test_parseWinningAndDrawn(self):
        actualWinners, actualDrawn = parseWinningAndDrawn(self.mockGame.split(":")[1])
        
        assert actualWinners == self.mockWinners
        assert actualDrawn == self.mockDrawn
        

    def test_parseGames(self):
        actualGameSplit = parseGames(self.mockGame)
        
        assert actualGameSplit == self.mockGameSplit
