"""
def max_sub_array_sum(my_list, n):
    max_sum = 0
    current_sum = 0
    for i in range(0, n):
        current_sum = current_sum + my_list[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum
"""

