def min_product_tuple(tup_list):
    min_product = (tup_list[0][0] * tup_list[0][1], tup_list[0][0], tup_list[0][1])
    for i in range(len(tup_list)):
        for j in range(i + 1, len(tup_list)):
            if tup_list[i][0] * tup_list[i][1] * tup_list[j][0] * tup_list[j][1] < min_product[0]:
                min_product = (tup_list[i][0] * tup_list[i][1] * tup_list[j][0] * tup_list[j][1], tup_list[i][0], tup_list[i][1], tup_list[j][0], tup_list[j][1])
    return min_product