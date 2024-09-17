def large_product(list1, list2, k):
    result = []
    for i in range(k):
        max_product = 0
        max_factor1 = None
        max_factor2 = None
        for factor1 in list1:
            for factor2 in list2:
                product = factor1 * factor2
                if product > max_product:
                    max_product = product
                    max_factor1 = factor1
                    max_factor2 = factor2
        result.append(max_product)
        list1.remove(max_factor1)
        list2.remove(max_factor2)
    return result