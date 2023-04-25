# Current chessboard pieces and positions 

chessboard = {
    'white': {
        '1a': 'wrook',
        '1b': 'wknight',
        '2e': 'wking'
    },

    'black': {
        '6a': 'bpawn',
        '7h': 'bbishop',
        '8d': 'bking'
    }
}

# Function to check validity of chessboard
# A valid board will have exactly one black king and one white king,
# each player can only have 16 pieces at most, at most 8 pawns and all pieces must be on a valid space from '1a' to '8h'. The piece
# The piece names must begin with 'w' or 'b' followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

def isValidChessboard(currentChessboard):
    # Check for kings (both black and white)
    for boardPlayer, boardPlayerDict in currentChessboard.items(): #boardPlayer stores the keys: "white" and "black". boardPlayerDict stores the nested dictionary. 
        #print(boardPlayer, boardPlayerDict)
        for chessPiecesPositions in boardPlayerDict: #Loop is still iterating through 'white'. The count for the 'for' loop is still 0. chessPiecesPositions stores the keys of the nested dictionary which are the chess piece positions.
            #print(chessPiecesPositions, boardPlayerDict[chessPiecesPositions])

            ### CHECKS FOR VALID BOARD ###

            # Check 1: 1 white king and 1 black king on board
            #print(boardPlayerDict[chessPiecesPositions])
            print(boardPlayerDict['1a'])
    
isValidChessboard(chessboard)