def prime_num(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

# Another solution
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Another solution
def is_prime_number(n):
    if(n < 2):
        return False
    if(n == 2):
        return True
    if(n % 2 == 0):
        return False
    i = 3
    while(i * i <= n):
        if(n % i == 0):
            return False
        i += 2
    return True

# Another solution
def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(n**0.5) + 1, 2): 
        if n % i == 0: 
            return False
    return True

# Another solution
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Another solution
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# Another solution
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Another solution
def is_prime(n):
    if n < 2: