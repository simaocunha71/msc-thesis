def replace_char(string,char,replace):
    res = ""
    for c in string:
        if c == char:
            res += replace
        else:
            res += c
    return res

# assert replace_char("polygon",'y','l')==("pollgon")



"""
Write a function to sort a list of tuples by a given element.
"""

def sort_by(lis,index):
    lis.sort(key = lambda x: x[index])

# sort_by([(2, 3), (1, 2), (3, 1)], 1)


"""
Write a function to calculate the sum of digits of a number.
"""

def sum_digits(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

# sum_digits(123)


"""
Write a function to calculate the product of digits of a number.
"""

def product_digits(n):
    res = 1
    while n:
        res *= n % 10
        n //= 10
    return res

# product_digits(123)


"""
Write a function to calculate the sum of all prime numbers less than n.
"""

def sum_primes(n):
    res = 0
    for i in range(2, n):
        if is_prime(i):
            res += i
    return res

# sum_primes(100)


"""
Write a function to check if a number is a prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# is_prime(