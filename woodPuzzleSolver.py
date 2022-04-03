from pieces import pieces, printPiece, printPieces
from prettyPrint import pp
from transaltor import translations
from overlapChecker import piecesOverlap
from combs import getCombs, getAllCombs
from rotator import turnPieceNTimes

def main ():
    positions = ['a', 'b', 'c', 'd', 'e', 'f']
    allMoveCombs = getCombs(positions)
    digits = [0, 1, 2, 3]
    allRotCombs = getAllCombs(digits, 6)

    for (i, moveComb) in enumerate(allMoveCombs):
        for rotComb in allRotCombs:
            # rotate pieces
            rotPieces = []
            for (pieceIdx, piece) in enumerate(pieces):
                turns = rotComb[pieceIdx]
                rotPiece = turnPieceNTimes(piece, turns)
                rotPieces.append(rotPiece)
            # move pieces
            movedPieces = []
            for (pieceIdx, piece) in enumerate(rotPieces):
                newPos = moveComb[pieceIdx]
                movedPiece = translations[newPos](piece)
                movedPieces.append(movedPiece)
            if not piecesOverlap(movedPieces):
                print('Success!', ''.join(moveComb), ' ', rotComb)
        if i % 25 == 0: print(i, 'tested')

def tmp ():
    printPieces(pieces)
    

    # testing rotation
    # piece = pieces[1]
    # for turns in range(4):
    #     rot = turnPieceNTimes(piece, turns)
    #     print(f'after {turns} turns:')
    #     printPiece(rot)


if (__name__ == '__main__'): main()
# if (__name__ == '__main__'): tmp()


