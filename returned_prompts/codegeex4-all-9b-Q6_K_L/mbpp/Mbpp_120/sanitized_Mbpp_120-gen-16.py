def max_product_tuple(test_list):
    product_list = []
    for i in range(len(test_list)):
        for j in range(i+1, len(test_list)):
            product_list.append(abs(test_list[i][0] * test_list[j][0]))
            product_list.append(abs(test_list[i][1] * test_list[j][1]))
    return max(product_list)