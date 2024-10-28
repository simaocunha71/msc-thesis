def max_product_tuple(tuple_list):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_product = 0
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            max_product = max(max_product, abs(tuple_list[i][0] * tuple_list[j][0]), abs(tuple_list[i][0] * tuple_list[j][1]),
                              abs(tuple_list[i][1] * tuple_list[j][0]), abs(tuple_list[i][1] * tuple_list[j][1]))
    return max_product
tuple_list = [(2, 7), (2, 6), (1, 8), (4, 9)]