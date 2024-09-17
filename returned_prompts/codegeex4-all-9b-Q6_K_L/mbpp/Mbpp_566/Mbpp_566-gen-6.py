def sum_digits(n: int) -> int:
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    return sum_of_digits

