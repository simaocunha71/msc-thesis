def large_product(list1, list2, n):
    products = [list1[i] * list2[j] for i in range(len(list1)) for j in range(len(list2))]
    return sorted(products, reverse=True)[:n]