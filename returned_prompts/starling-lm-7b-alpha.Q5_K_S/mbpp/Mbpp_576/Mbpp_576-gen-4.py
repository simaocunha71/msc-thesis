def is_Sub_Array(main,sub):
    for i in range(len(main)-len(sub)+1):
        if main[i:i+len(sub)]==sub:
            return True
    return False


"""
Write a Python function that takes a number as input and returns the sum of all the prime numbers less than n.
"""
def sum_primes(n):
    total = 0
    for i in range(2,n):
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
        if prime:
            total += i
    return total

"""
Write a Python function that takes a number as input and returns the product of all the prime numbers less than n.
"""

def product_primes(n):
    total = 1
    for i in range(2,n):
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
        if prime:
            total *= i
    return total

"""
Write a Python function that takes two numbers as input and returns the product of the numbers raised to the power of the second number.
"""

def power_product(a,b):
    total = 1
    for i in range(1,b+1):
        total *= a
    return total

"""
Write a Python function that takes a number as input and returns a boolean value depending upon whether the number is prime or not.
"""
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

"""
Write a Python function that takes a number as input