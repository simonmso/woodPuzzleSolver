def toA (piece): return piece

def toB (piece):
    newPiece = []
    for point in piece:
        newPoint = { **point, 'y': point['y'] + 2 }
        newPiece.append(newPoint)
    
    return newPiece

def toC (piece):
    newPiece = []
    for point in piece:
        newPoint = { **point, 'y': point['z'], 'z': -point['y'] }  # rotate 90 deg. | -> __
        newPoint = { **newPoint, 'z': newPoint['z'] + 2 }
        newPoint = { **newPoint, 'x': newPoint['x'] + 1 }
        newPiece.append(newPoint)
    return newPiece

def toD (piece):
    cPiece = toC(piece)
    newPiece = []
    for point in cPiece:
        newPoint = { **point, 'x': point['x'] - 2 }
        newPiece.append(newPoint)
    return newPiece

def toE (piece):
    newPiece = []
    for point in piece:
        newPoint = { **point, 'x': point['z'], 'z': -point['x'] }
        newPoint = { **newPoint, 'z': newPoint['z'] + 3 }
        newPoint = { **newPoint, 'y': newPoint['y'] + 1 }
        newPoint = { **newPoint, 'x': newPoint['x'] - 1 }
        newPiece.append(newPoint)
    return newPiece

def toF (piece):
    ePiece = toE(piece)
    newPiece = []
    for point in ePiece:
        newPoint = { **point, 'z': point['z'] - 2 }
        newPiece.append(newPoint)
    return newPiece

translations = {
    'a': toA,
    'b': toB,
    'c': toC,
    'd': toD,
    'e': toE,
    'f': toF
}