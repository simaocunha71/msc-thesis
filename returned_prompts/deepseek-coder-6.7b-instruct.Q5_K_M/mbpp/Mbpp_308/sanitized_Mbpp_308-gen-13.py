import itertools
def large_product(list1, list2, n):
    products = [i*j for i, j in itertools.product(list1, list2)]
    products.sort(reverse=True)
    return products[:n]