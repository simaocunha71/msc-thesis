def prime_num(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

# Driver Code
print(prime_num(13))



























"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Driver Code
print(is_prime(13))

"""



"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Driver Code
print(is_prime(13))
"""

"""
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Driver Code
print(is_prime(13))
"""

```























































































































































































