def sum_of_digits(lst):
    total = 0
    for i in lst:
        total += sum(map(int,str(i)))
    return total