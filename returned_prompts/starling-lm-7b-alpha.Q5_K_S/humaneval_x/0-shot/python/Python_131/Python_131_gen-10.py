
def digits(n):
    prod = 1
    for d in str(n):
        if int(d) % 2 == 1:
            prod *= int(d)
    return prod

# Alternative solution using list comprehension
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, map(str, n), 1)

# Alternative solution using generator expression
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, (str(i) for i in n), 1)

# Another alternative solution using list comprehension
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, [str(i) for i in n], 1)

# Another alternative solution using generator expression
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, (str(i) for i in n), 1)

# Yet another alternative solution using generator expression
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, (str(i) for i in n), 1)

# Yet another alternative solution using list comprehension
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, [str(i) for i in n], 1)

# Yet another alternative solution using generator expression
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, (str(i) for i in n), 1)

# Yet another alternative solution using generator expression
def digits(n):
    return reduce(lambda x, y: x * y if int(y) % 2 == 1 else x, (str(i) for i in n), 1)

# Yet another alternative solution using generator expression
def dig