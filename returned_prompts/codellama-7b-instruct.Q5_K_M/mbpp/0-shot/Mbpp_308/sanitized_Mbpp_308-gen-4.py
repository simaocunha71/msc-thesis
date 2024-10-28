def large_product(list1, list2, number_of_products):
    return sorted(list(zip(list1, list2)), key=lambda x: x[0] * x[1], reverse=True)[:number_of_products]