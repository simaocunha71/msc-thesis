def sum_of_digits(lst):
    res = []
    for i in lst:
        sum_digits = 0
        for digit in str(i):
            sum_digits += int(digit)
        res.append(sum_digits)
    return res

assert sum_of_digits([10,2,56]) == [1, 2, 11]


