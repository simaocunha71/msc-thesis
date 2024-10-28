def count_same_pair(l1, l2):
    return sum(x == y for x, y in zip(l1, l2))