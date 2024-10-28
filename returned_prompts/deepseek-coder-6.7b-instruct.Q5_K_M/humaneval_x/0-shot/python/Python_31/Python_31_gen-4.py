
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

#Python/prime_numbers_generator.py
def prime_numbers_generator(n):
    """
    A generator function to yield prime numbers up to n.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(n):
        if is_prime(num):
            yield num

#Python/prime_numbers_up_to_n.py
def prime_numbers_up_to_n(n):
    """
    Returns a list of prime numbers up to n.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(n) if is_prime(num)]

#Python/prime_numbers.py
from prime_numbers_up_to_n import prime_numbers_up_to_n
from prime_numbers_generator import prime_numbers_generator

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Prime numbers up to", n, ":")
    print(prime_numbers_up_to_n(n))
    print("Prime numbers up to", n, "(using generator):")
    for prime in prime_numbers_generator(n):
       