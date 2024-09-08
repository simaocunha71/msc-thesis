def multiply_num(lst):
    product = 1
    for i in lst:
        product *= i
    return product / len(lst)