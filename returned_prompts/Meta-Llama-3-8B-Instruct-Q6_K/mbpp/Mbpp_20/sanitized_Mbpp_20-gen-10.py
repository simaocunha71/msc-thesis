def is_woodall(n):
    s = 0
    sum_of_digits = sum(int(digit) for digit in str(n))
    for digit in str(n):
        s += int(digit) ** 2
    return s == sum_of_digits ** 2