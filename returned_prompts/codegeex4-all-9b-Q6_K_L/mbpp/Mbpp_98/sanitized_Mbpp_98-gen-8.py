def multiply_num(lst):
    if not lst:
        return 0
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)