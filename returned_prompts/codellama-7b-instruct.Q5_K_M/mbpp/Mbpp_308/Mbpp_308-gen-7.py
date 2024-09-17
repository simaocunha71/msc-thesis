
def large_product(list1, list2, n):
    return sorted([x * y for x in list1 for y in list2], reverse=True)[:n]


