def count_samepair(l1, l2, l3):
    return sum(x == y == z for x, y, z in zip(l1, l2, l3))