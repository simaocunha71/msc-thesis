def multiply_num(lst):
    if not lst:
        return 0
    total = 1
    for num in lst:
        total *= num
    return total / len(lst)