from pieces import pieces, printPiece
from prettyPrint import pp
from transaltor import translations
from overlapChecker import piecesOverlap
from combs import getCombs
from rotator import turnPieceNTimes

def main ():
    positions = ['a', 'b', 'c', 'd', 'e', 'f']
    allCombs = getCombs(positions)

    for (i, comb) in enumerate(allCombs):
        tmpPieces = []
        for (pieceIdx, piece) in enumerate(pieces):
            newPos = comb[pieceIdx]
            movedPiece = translations[newPos](piece)
            tmpPieces.append(movedPiece)
        if not piecesOverlap(tmpPieces):
            print('Success!', ''.join(comb))
        if i % 100 == 0: print(i, 'tested')

def tmp ():
    piece = pieces[1]
    for turns in range(4):
        rot = turnPieceNTimes(piece, turns)
        print(f'after {turns} turns:')
        printPiece(rot)


# if (__name__ == '__main__'): main()
if (__name__ == '__main__'): tmp()


