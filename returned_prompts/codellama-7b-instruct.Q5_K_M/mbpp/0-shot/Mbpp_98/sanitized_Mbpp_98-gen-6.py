from math import isnan
def multiply_num(my_list):
    if not my_list:
        return 0
    result = 1
    for num in my_list:
        result *= num
    if isnan(result):
        return 0
    return result / len(my_list)