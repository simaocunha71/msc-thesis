def large_product(list1, list2, n):
    products = [x*y for x in list1 for y in list2]
    return sorted(products, reverse=True)[:n]  # sort the products in descending order and return the top n products