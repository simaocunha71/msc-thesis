    def is_prime(n):
        """ Write a function that returns true if the given number is a prime number and false otherwise. """
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for divisor in range(3, sqrt_n, 2):
            if not n % divisor:
                return False
        return True

    for i in range(3, a):
        if a % i == 0:
            if is_prime(i):
                return False

    return True


