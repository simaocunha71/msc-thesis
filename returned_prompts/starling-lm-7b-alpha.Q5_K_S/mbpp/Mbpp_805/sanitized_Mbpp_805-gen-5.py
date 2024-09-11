from itertools import product
def max_sum_list(input_list):
    max_sum = 0
    max_sum_list = []
    for item in product(*input_list):
        if sum(item) > max_sum:
            max_sum = sum(item)
            max_sum_list = item
    return max_sum_list