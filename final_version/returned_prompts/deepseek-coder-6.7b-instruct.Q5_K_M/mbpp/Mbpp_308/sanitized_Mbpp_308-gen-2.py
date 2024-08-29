def large_product(list1, list2, num):
    products = []
    for i in list1:
        for j in list2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:num]