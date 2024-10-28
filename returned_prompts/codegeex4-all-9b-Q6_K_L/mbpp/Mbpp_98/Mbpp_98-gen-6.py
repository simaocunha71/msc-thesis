def multiply_num(num_list):
    from functools import reduce
    return reduce((lambda x, y: x * y), num_list) / len(num_list)

