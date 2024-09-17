def sum_of_digits(lst):
    return sum(sum(divmod(int(x), 10) for x in str(y)) for y in lst)