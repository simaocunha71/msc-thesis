def large_product(list1, list2, n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for _ in range(n):
        result.append(list1.pop(0) * list2.pop(0))
    return sorted(result, reverse=True)