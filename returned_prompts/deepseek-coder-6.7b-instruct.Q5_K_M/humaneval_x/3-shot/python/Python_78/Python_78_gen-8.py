    primes = {2, 3, 5, 7, 11, 13}
    hex_digits = {digit for digit in '0123456789ABCDEF'}
    return sum(1 for digit in num if int(digit, 16) in primes)


