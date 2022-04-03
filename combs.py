from prettyPrint import pp

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
