
def large_product(list1, list2, n):
    return sorted(map(lambda x: x[0] * x[1], zip(list1, list2))[-n:])


