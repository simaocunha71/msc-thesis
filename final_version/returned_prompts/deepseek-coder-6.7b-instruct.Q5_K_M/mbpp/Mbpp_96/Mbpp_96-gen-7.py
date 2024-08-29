def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

assert divisor(15) == 4


# Method 2:
def divisor(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

assert divisor(15) == 4


# Method 3:
def divisor(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

assert divisor(15) == 4


# Method 4:
def divisor(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

assert divisor(15) == 4


# Method 5:
def divisor(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

assert divisor(15) == 4


# Method 6:
def divisor(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

assert divisor(15) == 4


# Method 7:
def divisor(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

assert divisor(15