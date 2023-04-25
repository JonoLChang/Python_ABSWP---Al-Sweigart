# Current chessboard pieces and positions 

chessboard = {
    'white' : {
        '1a': 'wrook',
        '1b': 'wknight',
        '2e': 'wking',
        '6e': 'wking',
        '8c': 'wpawn'
    },

    'black' : {
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
    ### CHECK 1: Check for exactly 1 white king and 1 black king
    checkOne = True
    wkingCounter = 0
    bkingCounter = 0
    for chessPlayer, chessPlayerDict in currentChessboard.items():
        for chessPiecePosition in chessPlayerDict:
            if chessPlayerDict[chessPiecePosition] == 'wking':
                wkingCounter += 1
            if chessPlayerDict[chessPiecePosition] == 'bking':
                bkingCounter += 1
        if wkingCounter | bkingCounter > 1:
            checkOne = False
        #print(checkOne)

    ### CHECK 2: Check the number of pieces each player possesses
    checkTwo = True
    for chessPlayer in currentChessboard.keys():
        if len(currentChessboard[chessPlayer]) > 16:
            checkTwo =  False
    #print(checkTwo)

    ### CHECK 3: Checking for maximum limit on each type of chesspiece
    checkThree = True

    #Checking for maximum number of pawns (8)
    # want to check the number of times a pawn is occurring for each player. Should keep counter of when a pawn is checked.  
    wpawnCounter = 0
    bpawnCounter = 0
    for chessPlayerDict in currentChessboard.values():
        for chessPiecePosition in chessPlayerDict:
            if chessPlayerDict[chessPiecePosition] == 'wpawn':
                wpawnCounter += 1
            if chessPlayerDict[chessPiecePosition] == 'bpawn':
                bpawnCounter += 1
    if wpawnCounter | bpawnCounter > 8:
        checkThree = False
    #print(checkThree)

    ### CHECK 4: All piececs must be on a valid spaee i.e. '1a' to '8h'
    checkFour = True
    # Valid letter 'a' to 'h' 
    # Valid numbers '1' to '9'

    validNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for chessplayerDict in currentChessboard.values(): 
        for chessPiecePosition in chessplayerDict:
            if len(chessPiecePosition) < 3:
                if chessPiecePosition[0] not in validNumbers:
                    print(chessPiecePosition[0] + ' Invalid Number Position!')
                    checkFour = False
                else:
                    if chessPiecePosition[1] not in validLetters:
                        print(chessPiecePosition[1] + ' Invalid Letter Position!')
                        checkFour = False
            else:
                print('Invalid Positon!!')
                checkFour = False

    ### CHECK 5: Check piece names. Piece names must start with either 'w' or 'b' followed by 'pawn', 'knight', 'bishop', 'rook', 'queen' or 'king' 
    checkFive = True

    validPlayer = ['w', 'b']
    validChesspieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for chessPlayerDict in currentChessboard.values():
        for chessPiecePosition in chessPlayerDict:
            if chessPlayerDict[chessPiecePosition][0] not in validPlayer:
                checkFive = False
                #print(chessPiecePosition + " does not have a chesspiece that begins with 'w' or 'b'")
            elif chessPlayerDict[chessPiecePosition][1:] not in validChesspieces:
                checkFive = False
                # print('not valid')

    if True in {checkOne and checkTwo and checkThree and checkFour and checkFive}:
        print("Valid board!")
    else:
        print("Not a valid board!!!")

isValidChessboard(chessboard)