    from math import sqrt

    def is_prime(n):
        """
        Returns True if n is a prime number and False if it is not.
        """
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def is_multiply_prime(a):
        """
        Returns True if a is the product of exactly three distinct prime numbers in the range 2, a, and False otherwise.
        """
        if a < 3:
            return False
        if a < 9:
            return True
        if not a % 2:
            return False
        if not a % 3:
            return False
        if is_prime(a):
            return True
        while a % 2 == 0:
            a //= 2
        while a % 3 == 0:
            a //= 3
        return is_prime(a)

    return is_multiply_prime(a)

# Driver Program
a = 30
print(is_multiply_prime(a))



# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)





























































































































