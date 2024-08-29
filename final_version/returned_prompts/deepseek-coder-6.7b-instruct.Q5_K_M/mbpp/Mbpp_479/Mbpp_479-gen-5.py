def first_Digit(n):
    while n > 0:
        digit = n % 10
        n = n // 10
        if n > 0:
            continue
        else:
            return digit

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(str(n)[0])

print(first_Digit(123))

# OR

def first_Digit(n):
    n = str(n)
    for i in n:
        if i.isdigit():
            return int(i)

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(filter(str.isdigit, str(n))[0])

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(re.search(r'\d', str(n)).group())

print(first_Digit(123))

# OR

def first_Digit(n):
    return int("".join(filter(lambda x: x.isdigit(), str(n))))

print(first_Digit(123))

# OR

def first_Digit(n):
    return int(re.findall(r'\d', str(n))[0])

print(first_Digit(123))

# OR

def first_Digit(n):
    return int("".join(c for c in str(n) if c.isdigit()))

print(first_Digit(123))

# OR

def first_Digit(n):
    n = str(n)
    for i in range(len(n)):
        if n[i].isdigit():
            return int(n[i])

print(first_Digit(123))

# OR

def first_Digit(n):
    return next(int(i) for i in str(n) if i.isdigit())

print(first_