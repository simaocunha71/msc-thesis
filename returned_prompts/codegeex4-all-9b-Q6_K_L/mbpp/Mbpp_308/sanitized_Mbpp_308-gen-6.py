def large_product(list1, list2, n):
    result = []
    for i in range(n):
        product = max(list1) * max(list2)
        result.append(product)
        list1.remove(max(list1))
        list2.remove(max(list2))
    return result