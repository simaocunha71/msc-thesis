
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

assert power(3, 4) == 81

# Solution 2
def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a * a, b // 2)
    else:
        return a * power(a * a, (b - 1) // 2)

assert power(3, 4) == 81

# Solution 3
def power(a, b):
    return a ** b

assert power(3, 4) == 81

# Solution 4
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

assert power(3, 4) == 81

# Solution 5
def power(a, b):
    result = 1
    while b:
        if b & 1:
            result *= a
        b >>= 1
        a *= a
    return result

assert power(3, 4) == 81

# Solution 6
def power(a, b):
    return pow(a, b)

assert power(3, 4) == 81

# Solution 7
def power(a, b):
    return a << b if b >= 0 else a >> -b

assert power(3, 4) == 81

# Solution 8
def power(a, b):
    return functools.reduce(lambda x, _: x * a, range(b), 1)

assert power(3, 4) == 81

# Solution 9
def power(a, b):
    return math.pow(a, b)

assert power(3, 4) == 81

# Solution 10
def power(a, b):
    return Decimal(a) ** Decimal(b)

assert power(3, 4) == 81

