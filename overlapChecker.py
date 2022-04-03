def pointsAreSame(p1, p2):
    return p1['x'] == p2['x'] and p1['y'] == p2['y'] and p1['z'] == p2['z']


def piecesOverlap (pieces):
    filledPoints = []
    for piece in pieces:
        for p1 in piece:
            for p2 in filledPoints:
                if pointsAreSame(p1, p2): return True
            filledPoints.append(p1)
    
    return False

if (__name__ == '__main__'):
    print("This module has functions for checking if pieces overlap")
