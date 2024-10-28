def sum_digits(n):
    sum_num = 0
    while n:
        sum_num += n % 10
        n //= 10
    return sum_num