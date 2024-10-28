    even_indicies = [x for x in l[::2]]
    even_indicies.sort()
    for i in range(0, len(l), 2):
        l[i] = even_indicies[i//2]
    return l


