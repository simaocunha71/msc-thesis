def max_product_tuple(list_tuple):
    result = 0
    for i in range(len(list_tuple)):
        for j in range(i+1,len(list_tuple)):
            result = max(result, abs(list_tuple[i][0]*list_tuple[j][0]), abs(list_tuple[i][0]*list_tuple[j][1]), abs(list_tuple[i][1]*list_tuple[j][0]), abs(list_tuple[i][1]*list_tuple[j][1]))
    return result