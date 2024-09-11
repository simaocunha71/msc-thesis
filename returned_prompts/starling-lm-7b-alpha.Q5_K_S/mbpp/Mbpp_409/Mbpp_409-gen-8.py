def min_product_tuple(tup_list):
    min_product = (tup_list[0][0] * tup_list[0][1], tup_list[0][0], tup_list[0][1])
    for i in range(len(tup_list)):
        for j in range(i + 1, len(tup_list)):
            if tup_list[i][0] * tup_list[i][1] * tup_list[j][0] * tup_list[j][1] < min_product[0]:
                min_product = (tup_list[i][0] * tup_list[i][1] * tup_list[j][0] * tup_list[j][1], tup_list[i][0], tup_list[i][1], tup_list[j][0], tup_list[j][1])
    return min_product

if __name__ == '__main__':
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == (56, 2, 7, 1, 8)
    assert min_product_tuple([(2, 7), (1, 6), (1, 8), (4, 9)]) == (56, 2, 7, 1, 8)
    assert min_product_tuple([(1, 1), (2, 2), (3, 3), (4, 4)]) == (4, 1, 1, 2, 2)
    assert min_product_tuple([(1, 1), (1, 2), (1, 3), (1, 4)]) == (4, 1, 1, 2, 3)
    print('All tests passed.')


























"""


"""


"""





















"""


