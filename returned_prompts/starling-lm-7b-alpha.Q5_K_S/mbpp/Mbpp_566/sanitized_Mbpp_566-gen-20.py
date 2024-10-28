def sum_digits(num):
    """
    sum of digits of a non-negative integer
    """
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum