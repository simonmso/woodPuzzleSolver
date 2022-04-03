from prettyPrint import pp

pieces = [
    [ # 0
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 1},
        {'x': 0, 'y': 0, 'z': 2},
        {'x': 0, 'y': 0, 'z': 3},
        {'x': 0, 'y': 1, 'z': 0},
        {'x': 0, 'y': 1, 'z': 1},
        {'x': 0, 'y': 1, 'z': 2},
        {'x': 0, 'y': 1, 'z': 3},
        {'x': 1, 'y': 0, 'z': 0},
        {'x': 1, 'y': 0, 'z': 1},
        {'x': 1, 'y': 0, 'z': 2},
        {'x': 1, 'y': 0, 'z': 3},
        {'x': 1, 'y': 1, 'z': 0},
        {'x': 1, 'y': 1, 'z': 1},
        {'x': 1, 'y': 1, 'z': 2},
        {'x': 1, 'y': 1, 'z': 3}
    ],
    [ # 1
        {'x': 1, 'y': 0, 'z': 0},
        {'x': 1, 'y': 0, 'z': 1},
        {'x': 1, 'y': 0, 'z': 2},
        {'x': 1, 'y': 0, 'z': 3},
        {'x': 1, 'y': 1, 'z': 0},
        {'x': 1, 'y': 1, 'z': 1},
        {'x': 1, 'y': 1, 'z': 2},
        {'x': 1, 'y': 1, 'z': 3},
    ],
    [ # 2
        {'x': 1, 'y': 0, 'z': 0},
        {'x': 1, 'y': 0, 'z': 1},
        {'x': 1, 'y': 0, 'z': 2},
        {'x': 1, 'y': 0, 'z': 3},
        {'x': 1, 'y': 1, 'z': 0},
        {'x': 1, 'y': 1, 'z': 3},
    ],
    [ # 3
        {'x': 0, 'y': 1, 'z': 1},
        {'x': 0, 'y': 1, 'z': 2},
        {'x': 1, 'y': 0, 'z': 0},
        {'x': 1, 'y': 0, 'z': 3},
        {'x': 1, 'y': 1, 'z': 0},
        {'x': 1, 'y': 1, 'z': 1},
        {'x': 1, 'y': 1, 'z': 2},
        {'x': 1, 'y': 1, 'z': 3},
    ],
    [ # 4
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 3},
        {'x': 0, 'y': 1, 'z': 0},
        {'x': 1, 'y': 0, 'z': 0},
        {'x': 1, 'y': 0, 'z': 1},
        {'x': 1, 'y': 0, 'z': 2},
        {'x': 1, 'y': 0, 'z': 3},
        {'x': 1, 'y': 1, 'z': 0},
        {'x': 1, 'y': 1, 'z': 1},
    ],
    [  # 5
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 1},
        {'x': 0, 'y': 1, 'z': 0},
        {'x': 1, 'y': 0, 'z': 0},
        {'x': 1, 'y': 0, 'z': 1},
        {'x': 1, 'y': 0, 'z': 2},
        {'x': 1, 'y': 0, 'z': 3},
        {'x': 1, 'y': 1, 'z': 0},
        {'x': 1, 'y': 1, 'z': 3},
    ]
]

def p3D (threeArr):
    print(f"{'x = 0':6} {'x = 1':6}")
    for z in threeArr:
        print(f'{z[0]:6} {z[1]:6}')

square = '■'
endcap = []
for z in range(3):
    layer = []
    for i in range(2):
        layer.append(square * 2)
    endcap.append(layer)
space = ' '

def printPiece (piece):
    # layers[z][x][y]
    middle = []
    for _ in range(4):
        layer = []
        for _ in range(2):
            layer.append(space * 2)
        middle.append(layer)
    
    for pt in piece:
        temp = list(middle[3 - pt['z']][pt['x']])
        temp[pt['y']] = square
        middle[3 - pt['z']][pt['x']] = ''.join(temp)
    layers = endcap + middle + endcap
    p3D(layers)


def printPieces (ps):
    for (i, p) in enumerate(ps):
        print(f'Piece {i}:')
        printPiece(p)
        print()

if (__name__ == '__main__'):
    printPieces(pieces)