from prettyPrint import pp


# ex.
# abc, acb, cab, ...
# optionsArr = ['a', 'b', 'c']
# ret. [['a', 'b', 'c'], ['a', 'c', 'b'], ...]
def getCombs (optionsArr, curComb = []):
    allCombs = []
    shortenedArray = [ *optionsArr ]
    opt = shortenedArray.pop()
    for i in range(len(curComb) + 1):
        copy = curComb.copy()
        copy.insert(i, opt)
        if len(shortenedArray):
            newCombs = getCombs(shortenedArray, copy)
            allCombs.extend(newCombs)
        else:
            allCombs.append(copy)

    return allCombs

# ex.
# 000, 001, 002, 003, 010, 011, ...
# digits = [0, 1, 2, 3]
# places = 3
def getAllCombs (digits, places, curComb = []):
    allCombs = []
    if len(curComb) == places:
        allCombs.append(curComb)
    else:
        for digit in digits:
            newComb = [ *curComb ]
            newComb.append(digit)
            newCombs = getAllCombs(digits, places, newComb)
            allCombs += newCombs

    return allCombs