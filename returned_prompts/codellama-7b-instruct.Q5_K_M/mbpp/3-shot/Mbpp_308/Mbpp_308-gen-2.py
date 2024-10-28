
def large_product(list1, list2, n):
    result = []
    for i in range(n):
        result.append(list1[i] * list2[i])
    return sorted(result)[::-1]


