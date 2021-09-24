def main(n, ar):
    idx = dict()

    for i in ar:
        if i in idx:
            idx[i] += 1
        else: 
            idx[i] = 1

    print (idx)

if __name__ == "__main__":
    n = 6
    ar = [1, 2, 1, 2, 1, 3, 2]
    main(n, ar)

