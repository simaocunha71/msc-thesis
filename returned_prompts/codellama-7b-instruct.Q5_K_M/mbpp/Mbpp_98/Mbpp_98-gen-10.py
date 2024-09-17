
import math

def multiply_num(my_list):
    result = 1
    for num in my_list:
        result *= num
    result /= len(my_list)
    return result


