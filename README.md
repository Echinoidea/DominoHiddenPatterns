# Dominoes Hidden Patterns
## Introduction
This project aims to create a data set of _n_ recorded and encoded domino (block or draw) games. 
This data set will be used to predict the final layout of the game board and the winner of each game given the initial _n_ placed tiles.

## Game Parameters
Without the boundaries of a table or game board, the final layout of a dominoes game would always be a straight line.
In a game, if there is not enough room on the game board or table, the player may place the domino perpendicularly to the previous piece. 

Since dominoes doesn't have standard game board dimensions or tile dimensions, this presents a problem in how a model could predict the layout of a dominoes game. 
The final layout of a game played on a 20x20-inch board would differ significantly from a game played on a 30x30-inch board, or when played with different sized tiles.

To accommodate this, I will be using some parameters according to some tournament standards I found online. I'm also personally asking domino tournament hosts about their tournament standards
so I can make the most accurate replication of the game that I can. Meanwhile, these are the parameters I am using:
- Board size: 24x24-inches.
- Tile size: 2x1x0.5-inches.
- Cannot branch tiles off of an in-line, perpendicularly placed double tile.
- A game contains only one round.
- When placing a tile perpendicularly, the tile will be placed clockwise to the root piece if there is room, and counter-clockwise if there isn't..

## Questions/Hypothesis
**The initial _n_ placed tiles correlate to the final layout of the game board and to the winner of that round.**

**Additional questions**:
- How many potential combinations of moves are there in a standard game?
- How does the confidence of the prediction increase with each tile placed?
- What is the best/worst initial hand?
- What is the best/worst initial tile for player 1?
- Does each player have an equal probability of winning?

## The Data Set
The data will be stored in both CSV and JSON formats.
### Data Set Contents
- Game type (block, draw)
- Player count
- Initial hand size (7 or 5, dependent on player count)
- First player
- Initial _n_ played tiles
- All player's initial hands
- All player's skip count (if applicable)
- All player's draw count (if applicable)
- Encoded list of each turn's data (player turn, placed tile, skipped (if applicable), tile draw count (if applicable), remaining tiles in boneyard)
- Actual encoded final game board layout
- Actual winner
- Predicted encoded final game board layout
- Predicted winner
