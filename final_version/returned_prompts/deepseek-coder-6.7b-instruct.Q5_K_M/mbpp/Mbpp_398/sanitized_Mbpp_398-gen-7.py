def sum_of_digits(lst):
    res = []
    for i in lst:
        sum_digits = 0
        for digit in str(i):
            sum_digits += int(digit)
        res.append(sum_digits)
    return res