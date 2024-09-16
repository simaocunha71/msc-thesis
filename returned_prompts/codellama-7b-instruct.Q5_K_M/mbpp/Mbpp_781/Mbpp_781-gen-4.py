def count_divisors(n):
    return len(list(filter(lambda x: n % x == 0, range(1, int(n ** 0.5) + 1))))

def count_divisors(n):
    return sum(1 for i in range(1, int(n ** 0.5) + 1) if n % i == 0)

def count_divisors(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
    return cnt

def count_divisors(n):
    return sum(n % i == 0 for i in range(1, int(n ** 0.5) + 1))

def count_divisors(n):
    return sum(bin(n).count('1') - bin(i).count('1') for i in range(1, int(n ** 0.5) + 1))

def count_divisors(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
    return cnt

def count_divisors(n):
    return sum(bin(n).count('1') - bin(i).count('1') for i in range(1, int(n ** 0.5) + 1))

def count_divisors(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
    return cnt

def count_divisors(n):
    return sum(bin(n).count('1') - bin(i).count('1') for i in range(1, int(n ** 0.5) + 1))

def count_divisors(n):
    cnt = 0
    for i in range(1, int(n ** 0.5