def large_product(list1, list2, n):
    return sorted(map(lambda x,y: x*y, list1, list2), reverse=True)[:n]


