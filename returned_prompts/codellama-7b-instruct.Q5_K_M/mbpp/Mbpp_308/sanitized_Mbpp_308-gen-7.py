def large_product(list1, list2, n):
    assert n <= len(list1) and n <= len(list2)
    result = []
    for i in range(n):
        result.append(list1[i]*list2[i])
    return result