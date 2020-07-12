def has_negatives(a):

    dict = {}
    l = []
    for i in a:
        dict[i] = i
        if -i in dict and i != 0:
            l.append(abs(i))
    return l



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
