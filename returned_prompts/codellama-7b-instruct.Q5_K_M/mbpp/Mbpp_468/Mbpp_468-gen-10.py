"""
def max_product(my_list):
    max_product = 1
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            max_product = max(max_product, my_list[i] * my_list[j])
    return max_product
"""
