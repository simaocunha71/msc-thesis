def add_pairwise(tup):
    return tuple(tup[i] + tup[i + 1] for i in range(len(tup) - 1))

print(add_pairwise((1, 5, 7, 8, 10)))

