quarterTurnKey = [[{ 'x':0, 'y':1 }, { 'x':1, 'y':1 }], [{ 'x':0, 'y':0 }, { 'x':1, 'y':0}]]

def quarterTurn (piece):
    newPiece = []
    for pt in piece:
        newXY = quarterTurnKey[pt['x']][pt['y']]
        newPiece.append({ **pt,  **newXY })
        
    return newPiece

def turnPieceNTimes (piece, times):
    rotPiece = piece
    for _ in range(times):
        rotPiece = quarterTurn(rotPiece)
    return rotPiece