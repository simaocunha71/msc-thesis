def large_product(lst1, lst2, n):
    products = []
    for i in lst1:
        for j in lst2:
            products.append(i*j)
    products.sort(reverse=True)
    return products[:n]