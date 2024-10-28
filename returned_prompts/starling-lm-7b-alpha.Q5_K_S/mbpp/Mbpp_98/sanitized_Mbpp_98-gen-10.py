def multiply_num(lst):
    result = 1
    for item in lst:
        result *= item
    return result/len(lst)