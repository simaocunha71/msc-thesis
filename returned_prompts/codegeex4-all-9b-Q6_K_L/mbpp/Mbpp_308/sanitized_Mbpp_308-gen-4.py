def large_product(list1, list2, count):
    result = []
    for i in range(count):
        max_product = 0
        for a in list1:
            for b in list2:
                product = a * b
                if product > max_product:
                    max_product = product
        result.append(max_product)
        list1.remove(max_product // a)
        list2.remove(max_product // b)
    return result