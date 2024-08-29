def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))


