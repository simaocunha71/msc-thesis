def first_Digit(n):
    n = abs(n)
    while n > 0:
        digit = n % 10
        n = n // 10
        return digit
    return None

print(first_Digit(123))

# OR

def first_Digit(n):
    n = abs(n)
    str_n = str(n)
    return int(str_n[0])

print(first_Digit(123))

# OR

def first_Digit(n):
    n = str(n)
    for char in n:
        if char.isdigit():
            return int(char)

print(first_Digit(123))

# OR

def first_Digit(n):
    n = str(n)
    return int(next(filter(str.isdigit, n)))

print(first_Digit(123))

# OR

import re
def first_Digit(n):
    return int(re.search(r'\d', str(n)).group())

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(next(c for c in str(n) if c.isdigit()))

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(filter(lambda c: c.isdigit(), str(n))[0])

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(next(c for c in str(abs(n)) if c.isdigit()))

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(next(filter(str.isdigit, str(abs(n)))))

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(next(filter(str.isdigit, str(n))))

