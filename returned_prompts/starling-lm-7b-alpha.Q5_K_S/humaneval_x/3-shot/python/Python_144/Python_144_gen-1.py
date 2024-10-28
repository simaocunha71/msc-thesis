    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))

    lcm = denominator_x * denominator_n // gcd(denominator_x, denominator_n)

    if (numerator_x * denominator_n + numerator_n * denominator_x) % lcm == 0:
        return True
    else:
        return False


# Helper function to calculate the GCD of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_prime(n):
    """ Returns True if the number is prime, and False otherwise """

    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    """ Returns the smallest prime number greater than n """

    if n <= 1:
        return 2
    if is_prime(n):
        return n + 1
    n += 1
    while not is_prime(n):
        n += 1
    return n


def prime_factors(n):
    """ Returns a list of prime factors of a number """

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def divisors(n):
    """ Returns a sorted list of divisors of a number """

    factors = prime_factors(n