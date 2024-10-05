    evens = [l[i] for i in range(0, len(l), 2)]
    evens.sort()

    result = [None] * len(l)
    result[::2] = evens
    result[1::2] = l[1::2]

    return result


