"""
def newman_prime(n):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    count = 0
    number = 2
    while True:
        if is_prime(number):
            count += 1
            if count == n:
                return number
        number += 1
"""

