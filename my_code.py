def main(n, pairs):
    mapPairs = dict()

    for i in pairs:
        if i in mapPairs:
            mapPairs[i] += 1
        else: 
            mapPairs[i] = 1

    print (mapPairs)

    contador = 0
    for i in mapPairs:
        contador += int(mapPairs[i]/2)

    print (contador)

if __name__ == "__main__":
    n = 6
    ar = [1, 2, 1, 2, 1, 3, 2]
    main(n, ar)

