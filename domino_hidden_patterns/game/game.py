from deck import Deck
from tile import Tile
from enums.orientations import Orientation
from player import Player
from snake import Snake

from random import randint
from typing import NamedTuple

class RoundWinner(NamedTuple):
    player: Player
    pointsToGain: int


class Game:
    
    def __init__(self):
        self.playerScores = {'1': 0, '2': 0}  # Retain total points gained over rounds
        self.scoreToWin = 30
        
        self.roundCounter = 0
        self.deck = Deck()
        
        self.player1 = Player(self.deck, '1')
        # self.player1.points = self.playerScores['1']
        
        self.player2 = Player(self.deck, '2')
        # self.player2.points = self.playerScores['2']
        
        self.snake = Snake()
        self.turn = 1
        
        # Variables for encoder. Not the best solution, but it's ok
        self.playerDrawCountsTotal = {'1': 0, '2': 0}
        self.playerPassCountsTotal = {'1': 0, '2': 0}

        self.drawCountCurrent = 0
        self.hasPassedThisTurn = False
    
    
    def startRound(self):
        """Start a new round. Resets Deck, Player data (retains points), 
        Snake, and sets turn priority to last winner.
        """
        
        self.deck = Deck()
        
        self.player1 = Player(self.deck, '1')
        self.player1.points = self.playerScores['1']
        
        self.player2 = Player(self.deck, '2')
        self.player2.points = self.playerScores['2']
        
        self.snake = Snake()
        self.snake.setStartPiece(self.deck)
        
        self.roundCounter += 1
        self.initialTurn = self.getInitialTurn()
        self.turn = self.initialTurn if self.roundCounter <= 1 else self.getLastRoundWinnerId()
        
        
    
    def getInitialTurn(self) -> int:
        """Decide which Player goes first based on how you would in the real game.
        Both Players draw a Tile. The Player whose Tile contains the most pips goes first.
        If it's a draw, flip a coin for who goes first.

        Returns:
            int: The decided inital turn
        """
        
        rTile1 = self.deck.getRandomTile()
        rTile2 = self.deck.getRandomTile()
        
        rTile1Sum = rTile1.pip1 + rTile1.pip2
        rTile2Sum = rTile2.pip1 + rTile2.pip2
        
        print("Player 1 and 2's selected Tile values: {} vs {}".format(rTile1Sum, rTile2Sum))
        if rTile1Sum > rTile2Sum:
            print("Player 1 goes first")
            return 1
        elif rTile2Sum > rTile1Sum:
            print("Player 2 goes first")
            return 2
        else:
            coin = randint(1, 2)
            print("Draw. Coin flip to decide who plays first.\nPlayer {} goes first".format(coin))
            return coin

    
    def checkRoundWin(self) -> bool:
        """Check if a Play has won the round by having 0 Tiles in their hand.

        Returns:
            bool: True if either Player has no Tiles in their hands.
        """
        
        return self.player1.countTilesInHand() <= 0 or self.player2.countTilesInHand() <= 0
    
    
    def checkMatchWin(self) -> bool:
        """Check if either Play has won the match by reaching the scoreToWin.

        Returns:
            bool: True if either Player.points >= this Game's scoreToWin.
        """
        
        return self.playerScores['1'] >= self.scoreToWin or self.playerScores['2'] >= self.scoreToWin
    
    
    def getRoundWinner(self) -> RoundWinner:
        """Check if either Player has no Tiles left in their hand. If so, return a
        named tuple containing the winning Player obj and the total number of pips
        in the opponents hand for score calculation.

        Returns:
            RoundWinner: Custom NamedTuple containing the winning Player and the total 
            number of pips in the opposing Player's hand.
        """
        
        if self.player1.countTilesInHand() <= 0:
            pointsToGain = self.player2.countPipsInHand()
            self.playerScores['1'] += pointsToGain
            return RoundWinner(self.player1, pointsToGain)
        else:
            pointsToGain = self.player1.countPipsInHand()
            self.playerScores['2'] += pointsToGain
            return RoundWinner(self.player2, pointsToGain)
        
        
    def getMatchWinner(self) -> Player:
        """Runs getRoundWinner() internally. If the points added to the winner by getRoundWinner()
        exceeds the pointsToWin, return the Player that has won the match.

        Returns:
            Player: The Player that has won the match.
        """
        
        if self.playerScores['1'] >= self.scoreToWin:
            return self.player1
        elif self.playerScores['2'] >= self.scoreToWin:
            return self.player2
        
        # winner = self.getRoundWinner().player
        
        # if winner.points >= self.scoreToWin:
        #     return winner
        # else:
        #     return
        
        
    def getLastRoundWinnerId(self) -> int:
        """Get the ID of the Player that is returned by getRoundWinner()
        Used to set the turn priority of a new round to be the previous winner.

        Returns:
            int: The ID of the Player returned by getRoundWinner().
        """
        
        winner = self.getRoundWinner()
        return winner.player.id
    
        
    def playTile(self, player: Player, tile: Tile, side: Orientation):
        """Play and remove a Tile from the Player's hand and add it to the Snake.

        Args:
            player (Player): The Player that is playing a Tile.
            tile (Tile): The Tile to be played.
            side (Orientation): Which endpoint of the Snake to add the Tile to.
        """
        
        assert side in [Orientation.LEFT, Orientation.RIGHT], 'Side to add Tile to must be LEFT or RIGHT'

        self.snake.addTile(tile, side)
        player.removeTileFromHand(tile)
    
    
    def skipTurn(self):
        """Swap the value of turn from 1 to 2, or vice versa.
        """
        
        # self.turn = 1 if self.turn == 2 else 2
        self.drawCountCurrent = 0
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
    
    
    def mustDraw(self, player: Player) -> bool:
        """Check if the Player's hand contains any Tiles that can match those on this
        Game's Snake.

        Args:
            player (Player): The Player who is attempting to place a Tile.

        Returns:
            bool: True if the Player has no available moves and must draw from the Deck.
        """
        
        for tile in player.hand:
            if self.snake.canAddTile(tile):
                return False
            else:
                continue
        
        return True

    
    def mustSkipTurn(self, player: Player) -> bool:
        if not self.deck.isDeckEmpty():
            return False
        
        for tile in player.hand:
            if self.snake.canAddTile(tile):
                return False
        
        return True


    def drawUntilValidTile(self, player: Player):
        """Draw Tiles until there is a playable Tile in the Player's hand.

        Args:
            player (Player): The Player who needs to draw Tiles.
        """
        
        self.drawCountCurrent = 0
        self.hasPassedThisTurn = False
        
        while self.mustDraw(player):
            if self.deck.isDeckEmpty():
                # print("Deck is empty. Turn must be skipped.")
                self.playerPassCountsTotal[str(self.turn)] += 1
                self.hasPassedThisTurn = True
                return
            
            self.playerDrawCountsTotal[str(self.turn)] += 1
            self.drawCountCurrent += 1
            
            player.drawFromDeck()
            player.printHand()
            
    
    def isTie(self):
        return self.mustSkipTurn(self.player1) and self.mustSkipTurn(self.player2)