    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(hex.count(digit) for digit in primes)


