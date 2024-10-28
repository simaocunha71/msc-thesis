def large_product(list1, list2, n):
    if n > len(list1) * len(list2):
        return "Error: n is larger than the total number of combinations"
    products = [(a, b) for a in list1 for b in list2]
    products.sort(key=lambda x: x[0]*x[1], reverse=True)
    return [x[0]*x[1] for x in products[:n]]