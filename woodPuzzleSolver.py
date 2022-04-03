from pieces import pieces
from prettyPrint import pp
from transaltor import translations
from overlapChecker import piecesOverlap
from combs import getCombs

def getAllOrientations ():
    return getCombs(positions)


if (__name__ == '__main__'):
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



    # for piece in pieces:
    #     for pos in positions:
    #         p1 = translations[pos](piece)


    # # for translator debugging:
    # t = translations['f'](pieces[1])
    # print()
    # print('piece -> translated')
    # for (i, point) in enumerate(pieces[1]):
    #     print(f'{point}  ->  {t[i]}')

    # print()

