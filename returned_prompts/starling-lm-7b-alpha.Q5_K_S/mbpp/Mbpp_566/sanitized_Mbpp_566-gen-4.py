def sum_digits(n):
    result = 0
    while n:
        result += n % 10
        n = n // 10
    return result