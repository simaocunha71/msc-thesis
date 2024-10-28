def find_dissimilar(t1, t2):
    set1 = set(t1)
    set2 = set(t2)
    dissimilar = (element for element in set1.union(set2) if element not in set1.intersection(set2))
    return tuple(sorted(dissimilar))