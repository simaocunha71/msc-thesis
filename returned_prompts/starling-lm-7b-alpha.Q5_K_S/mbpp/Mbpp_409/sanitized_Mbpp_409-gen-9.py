def min_product_tuple(list_tuple):
    list_tuple.sort(key = lambda x : x[0]*x[1])
    return list_tuple[0][0]*list_tuple[0][1]