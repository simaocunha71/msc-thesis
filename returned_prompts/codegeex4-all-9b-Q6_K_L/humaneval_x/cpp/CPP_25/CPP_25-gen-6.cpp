def factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i== 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes

B:
def factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes

C:
def factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes

D:
def factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes

E:
def factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes

F:
def factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2