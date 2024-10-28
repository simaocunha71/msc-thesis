    primes = {2, 3, 5, 7, 11, 13}
    hex_digits = {char for char in '0123456789ABCDEF'}
    return sum(1 for char in num if int(char, 16) in primes)


