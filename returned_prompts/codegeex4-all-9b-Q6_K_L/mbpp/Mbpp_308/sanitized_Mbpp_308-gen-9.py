def large_product(list1, list2, n):
    result = []
    for i in range(n):
        max_product = max(x * y for x in list1 for y in list2)
        result.append(max_product)
        list1.remove(max_product // max(list1))
        list2.remove(max_product // max(list2))
    return result