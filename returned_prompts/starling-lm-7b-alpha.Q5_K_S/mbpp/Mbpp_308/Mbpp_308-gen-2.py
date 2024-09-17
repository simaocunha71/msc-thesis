
def large_product(list1, list2, n):
    list1.sort()
    list2.sort()
    result = []
    for i in range(n):
        result.append(list1[i] * list2[i])
    result.sort(reverse=True)
    return result


