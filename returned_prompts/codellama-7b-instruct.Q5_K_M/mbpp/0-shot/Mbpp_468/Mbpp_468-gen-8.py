"""
# O(n) time and O(n) space
def max_product(my_list):
    n = len(my_list)
    if n == 0:
        return 0
    elif n == 1:
        return my_list[0]
    else:
        max_product = my_list[0]
        for i in range(1, n):
            if my_list[i] > max_product:
                max_product = my_list[i]
        for i in range(n-1, -1, -1):
            if my_list[i] > max_product:
                max_product = my_list[i]
        return max_product
"""