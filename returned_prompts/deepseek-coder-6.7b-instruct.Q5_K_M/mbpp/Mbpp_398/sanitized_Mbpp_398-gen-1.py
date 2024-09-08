def sum_of_digits(lst):
    return [sum(map(int, str(i))) for i in lst]