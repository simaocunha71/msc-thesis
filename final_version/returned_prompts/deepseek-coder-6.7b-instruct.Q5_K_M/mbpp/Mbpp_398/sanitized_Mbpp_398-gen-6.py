def sum_of_digits(lst):
    res = []
    for num in lst:
        sum_digits = 0
        while num > 0:
            digit = num % 10
            sum_digits += digit
            num //= 10
        res.append(sum_digits)
    return res