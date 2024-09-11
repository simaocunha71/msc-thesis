"""
def count_divisors(n):
    if n == 0:
        return 0
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False


assert count_divisors(10)
"""

def count_divisors(n):
    if n == 0:
        return 0
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False


assert count_divisors(10)


# Python program to check if a number is prime
def isPrime(n):
    # Check if number is less than 2
    if (n <= 1):
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


assert count_divisors(10)


# Python program to find the divisors of a number
def Divisors(n):
    l = []
    # Note that this loop runs till square root
    for i in range(1, int(n ** 0.5) + 1):
        if (n % i == 0):
            # If divisors are equal, print only one
            if (n / i == i):
                l.append(i)
            else:  # Otherwise print both
                l.append(i)
                l.append(n // i)
    return l


def count_divisors(n):
    return len(Divisors(n))


assert count_divisors(10)

# Python program to check if a number is prime
def isPrime(n):
    # Check if number is less than 2
    if (n <= 1):
        return False
    # Check from