def sum_digits(num):
    summ = 0
    while num:
        summ += num % 10
        num //= 10
    return summ