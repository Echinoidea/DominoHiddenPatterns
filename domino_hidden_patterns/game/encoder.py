from game import Game
from tile import Tile
from snake import Snake
from player import Player
from deck import Deck

import pandas as pd
from dataclasses import dataclass

@dataclass
class EncodedTile:
    pips: ()
    encoded: str


@dataclass
class EncodedSnake:
    snakeDict: {}
    encoded: str


class Encoder:
    """Encode all game data for each turn similar to algebraic chess notation for use in learning model.
    Save outputs in JSON format and CSV. 
    
    Records and encodes the following information:
    - Match scope (recorded at the end of a match):
        - First player
        - Players initial hands
        - Players total draw count
        - Players total turn pass count
        - Number of rounds and the winner for each
        
    - Round scope (recorded at the end of a round):
        - Each player's points at the end of each round
        - The initial piece played
        - The final layout of the snake
    
    - Start turn scope (recorded at the beginning of each turn):
        - The deck contents
        - Each player's hands
        - The snake layout
    
    - End turn scope (recorded at the end of each turn):
        - The deck contents
        - Each player's hands
        - The snake layout
        - Number of Tiles drawn
        - Turn pass boolean
    """
    
    def __init__(self):
        self.matchDf = pd.DataFrame()
        self.roundDf = pd.DataFrame()
        self.turnStartDf = pd.DataFrame()
        self.turnEndDf = pd.DataFrame()
    
    
    def encodeTile(self, tile: Tile) -> EncodedTile:
        """Encode a Tile.
        E.g. Tile(1, 2), orientation => '1|2'

        Args:
            tile (Tile): The Tile to encode.

        Returns:
            EncodedTile: EncodedTile object containing the original pip values and the 
            encoded string.
        """
        
        return "{}|{}".format(tile.pip1, tile.pip2)
    
    
    def encodeSnakeLayout(self, snake: Snake, split=" ") -> EncodedSnake:
        """Encode a Snake's dict contents.
        E.g. {-1: Tile(1, 2), 0: Tile(2, 3), 1: Tile(3, 4)} => "-1:1|2 0:2|3 1:3|4"

        Args:
            snake (Snake): The Snake object to encode.

        Returns:
            EncodedSnake: EncodedSnake object containing the original snake dict value and 
            the encoded string.
        """
        
        encoded = []
        
        for key, tile in snake.snake.items():
            encoded.append("{}:{}".format(key, self.encodeTile(tile)))
        
        return split.join(encoded)  
    
    
    def encodeHandContents(self, player: Player, split=" "):
        
        
        encoded = []
        
        for tile in player.hand:
            encoded.append(self.encodeTile(tile))
        
        return split.join(encoded)        
    
    
    def encodeDeckContents(self, deck: Deck, split=" "):
        
         
        encoded = []
        
        for tile in deck.deck:
            encoded.append(self.encodeTile(tile))
            
        return split.join(encoded)
    
    
    def recordMatchData(self, game: Game):
        '''
        - First player
        - Players total draw count
        - Players total turn pass count
        - Number of rounds and the winner for each
        '''
        
        matchData = {}
        
        matchData["initialTurn"] = game.initialTurn
        matchData["player1DrawCount"] = game.playerDrawCountsTotal['1']
        matchData["player2DrawCount"] = game.playerDrawCountsTotal['2']
        matchData["player1PassCount"] = game.playerPassCountsTotal['1']
        matchData["player2PassCount"] = game.playerPassCountsTotal['2']
        matchData["roundCount"] = game.roundCounter
        
        row = pd.DataFrame([matchData])
        self.matchDf = pd.concat([self.matchDf, row], ignore_index=True)
    
    
    def recordRoundData(self, game: Game):
        '''
        - Each player's points at the end of each round
        - The initial piece played
        - The final layout of the snake
        '''
        
        roundData = {}
        
        # When writing to csv, 'initialTurn' turns into 'NoneialTurn'???
        roundData["initialTurn"] = game.initialTurn
        roundData["player1Points"] = game.player1.points
        roundData["player2Points"] = game.player2.points
        roundData["initialTile"] = self.encodeTile(game.snake.snake[0])
        roundData["snakeLayout"] = self.encodeSnakeLayout(game.snake)
        
        row = pd.DataFrame([roundData])
        self.roundDf = pd.concat([self.roundDf, row], ignore_index=True)
        
    
    def recordTurnStartData(self, game: Game):
        '''
        - The player turn
        - The deck contents
        - Each player's hands
        - The snake layout
        '''
        
        turnStartData = {}
        
        # When saving to CSV, 'playerTurn' turns into NoneerTurn???
        turnStartData["playerTurn"] = game.turn
        turnStartData["deckContents"] = self.encodeDeckContents(game.deck)
        turnStartData["player1Hand"] = self.encodeHandContents(game.player1)
        turnStartData["player2Hand"] = self.encodeHandContents(game.player2)
        turnStartData["snakeContents"] = self.encodeSnakeLayout(game.snake)
        
        row = pd.DataFrame([turnStartData])
        self.turnStartDf = pd.concat([self.turnStartDf, row], ignore_index=True)
    
    
    def recordTurnEndData(self, game: Game):
        '''
        - The player turn
        - The deck contents
        - Each player's hands
        - The snake layout
        - Number of Tiles drawn
        - Turn pass boolean
        '''

        turnEndData = {}

        turnEndData["playerTurn"] = game.turn
        turnEndData["deckContents"] = self.encodeDeckContents(game.deck)
        turnEndData["player1Hand"] = self.encodeHandContents(game.player1)
        turnEndData["player2Hand"] = self.encodeHandContents(game.player2)
        turnEndData["snakeContents"] = self.encodeSnakeLayout(game.snake)
        turnEndData["tilesDrawnCount"] = game.drawCountCurrent
        turnEndData["passedTurn"] = game.hasPassedThisTurn
        
        row = pd.DataFrame([turnEndData])
        self.turnEndDf = pd.concat([self.turnEndDf, row], ignore_index=True)
    
    
    def saveDfToJSON(self, df: pd.DataFrame, path: str):
        try:
            with open(path, 'w') as f:
                f.write(str(df.to_json(path, orient='records', lines=True)))
        except Exception as e:
            print(e.args)
    
    
    def saveDfToCSV(self, df: pd.DataFrame, path: str):
        try:
            with open(path, 'w') as f:
                f.write(str(df.to_csv(path, encoding='utf-8', index=False)))
        except Exception as e:
            print(e.args)
        


# g = Game()
# encoder = Encoder()

# encoder.recordRoundData(g)
# print(encoder.roundDf.head())
# encoder.saveDfToCSV(encoder.roundDf, 'round.csv')
# encoder.saveDfToJSON(encoder.roundDf, 'round.json')