def sum_negativenum(lst):
    return sum(i for i in lst if i < 0)

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

