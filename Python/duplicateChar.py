a = "abcdeafabd"

def duplicateChar(a):
    b = list(a)
    
    countDist = {}

    for i in b:
        if i in countDist:
            countDist[i] = countDist[i] + 1
        else:
            countDist[i] = 1

    print(countDist)

duplicateChar(a)