def sum_of_digits(lst):
    sums = 0
    for i in lst:
        while i:
            sums += i % 10
            i //= 10
    return sums