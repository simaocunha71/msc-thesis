
import itertools as it
def large_product(list1, list2, n):
    products = sorted([a*b for a, b in it.product(list1, list2)], reverse=True)
    return products[:n]


