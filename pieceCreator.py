from prettyPrint import pp

if (__name__ == '__main__'):
    piece = []

    for x in range(2):
        for y in range(2):
            for z in range(4):
                filled = input(f'filled at ({x}, {y}, {z})?')
                if filled == 'y': piece.append({ 'x': x, 'y': y, 'z': z })

    pp(piece)
