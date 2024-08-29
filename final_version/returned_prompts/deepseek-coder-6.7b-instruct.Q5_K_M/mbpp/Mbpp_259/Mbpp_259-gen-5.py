def maximize_elements(tup1, tup2):
    return tuple(tuple(max(x, y) for x, y in zip(a, b)) for a, b in zip(tup1, tup2))

print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))


