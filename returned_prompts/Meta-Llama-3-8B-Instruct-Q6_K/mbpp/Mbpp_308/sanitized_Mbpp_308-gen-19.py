def large_product(list1, list2, n):
    products = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            products.append(list1[i] * list2[j])
    return sorted(products, reverse=True)[:n]