def sum_of_digits(lst):
    res = []
    for num in lst:
        sum_digits = 0
        for digit in str(num):
            sum_digits += int(digit)
        res.append(sum_digits)
    return res