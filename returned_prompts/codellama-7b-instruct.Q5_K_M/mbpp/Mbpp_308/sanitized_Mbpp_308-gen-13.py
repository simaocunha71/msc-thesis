def large_product(list1, list2, n):
    list1 = sorted(list1, reverse=True)
    list2 = sorted(list2, reverse=True)
    return [list1[i] * list2[i] for i in range(n)]