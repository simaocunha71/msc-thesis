

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            if i > biggest_factor:
                bigger = True
                break
            else:
                bigger = False
                continue
            factor = i
            if not big_list:
                big_list = []
            if bigger and isinstance(biggest, int):
                big_list.append(biggest)
                biggest = n/factor
            elif not bigger:
                big_list.append((n//i, i))
                biggest = factor
    return biggest
