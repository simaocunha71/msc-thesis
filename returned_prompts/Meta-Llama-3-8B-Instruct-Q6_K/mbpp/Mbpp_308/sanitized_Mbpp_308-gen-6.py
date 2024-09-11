import heapq as hq
def large_product(list1, list2, n):
    products = [(a * b, a, b) for a in list1 for b in list2]
    return [a * b for a, b in hq.nlargest(n, products)[n:]]