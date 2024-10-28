def sum_negativenum(lst):
    sum = 0
    for num in lst:
        if num < 0:
            sum += num
    return sum