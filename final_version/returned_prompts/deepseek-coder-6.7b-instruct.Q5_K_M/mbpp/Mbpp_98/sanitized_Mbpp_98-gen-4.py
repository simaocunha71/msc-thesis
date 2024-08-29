def multiply_num(lst):
    mult = 1
    for num in lst:
        mult *= num
    return mult / len(lst)