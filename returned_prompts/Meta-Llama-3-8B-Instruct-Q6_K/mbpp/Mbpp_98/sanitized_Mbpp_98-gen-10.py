import math
def multiply_num(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result / len(num_list) if num_list else 0