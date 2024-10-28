def large_product(list1: list, list2: list, n: int) -> list:
    products = []
    for num1 in list1:
        for num2 in list2:
            products.append(num1 * num2)
    products.sort(reverse=True)
    return products[:n]