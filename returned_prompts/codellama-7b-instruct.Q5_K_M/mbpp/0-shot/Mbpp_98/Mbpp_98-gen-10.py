def multiply_num(my_list):
    if not my_list:
        return None
    result = 1
    for num in my_list:
        result *= num
    return result / len(my_list)
