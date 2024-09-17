def is_woodall(n):
    total = 0
    while n > 0:
        digit = n % 10
        if digit > 4:
            digit = 9 - digit
        total += digit
        n //= 10
    return total % 3 == 0