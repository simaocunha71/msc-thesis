"""
def odd_length_sum(my_list):
    odd_sum = 0
    for i in range(1, len(my_list)):
        for j in range(i, len(my_list)):
            odd_sum += my_list[i] + my_list[j]
    return odd_sum
"""
