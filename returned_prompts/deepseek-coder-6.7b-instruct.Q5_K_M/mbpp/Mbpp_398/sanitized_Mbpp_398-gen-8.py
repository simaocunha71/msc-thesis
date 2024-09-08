def sum_of_digits(lst):
    return [sum(int(i) for i in str(n)) for n in lst]