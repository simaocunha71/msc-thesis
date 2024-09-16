def find_Index(n):
    number = 1
    while len(str(number)) < n:
        number += 1
    return len(str(number))

# 2.
def find_Index(n):
    number = 1
    for i in range(n):
        number += 1
    return len(str(number))

# 3.
def find_Index(n):
    number = 1
    while len(str(number)) < n:
        number += 1
    return len(str(number)) - 1

# 4.
def find_Index(n):
    number = 1
    for i in range(n - 1):
        number += 1
    return len(str(number)) - 1

# 5.
def find_Index(n):
    number = 1
    while len(str(number)) < n - 1:
        number += 1
    return len(str(number))

# 6.
def find_Index(n):
    number = 1
    for i in range(n - 2):
        number += 1
    return len(str(number))

# 7.
def find_Index(n):
    number = 1
    while len(str(number)) < n - 2:
        number += 1
    return len(str(number))

# 8.
def find_Index(n):
    number = 1
    for i in range(n - 3):
        number += 1
    return len(str(number))

# 9.
def find_Index(n):
    number = 1
    while len(str(number)) < n - 3:
        number += 1
    return len(str(number))

# 10.
def find_Index(n):
    number = 1
    for i in range(n - 4):
        number += 1
    return len(str(number))

# 11.
def find_Index(n):
    number = 1
    while len(str(number)) < n - 4: