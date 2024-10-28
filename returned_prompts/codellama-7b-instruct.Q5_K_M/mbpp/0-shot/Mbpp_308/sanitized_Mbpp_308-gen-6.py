def large_product(list1, list2, k):
    return sorted(list(map(lambda x, y: x * y, list1, list2)), reverse=True)[:k]