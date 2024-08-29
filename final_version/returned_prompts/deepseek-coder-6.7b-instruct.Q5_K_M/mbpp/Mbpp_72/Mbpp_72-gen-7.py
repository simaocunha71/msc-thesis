def dif_Square(n):
    i = 0
    while i <= n:
        j = 0
        while j <= n:
            if i*i - j*j == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5)) # True

# Solution 2
def dif_Square(n):
    i = 0
    while i*i <= n:
        j = 0
        while j*j <= n:
            if i*i - j*j == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5)) # True

# Solution 3
def dif_Square(n):
    i = 0
    while i*i <= n:
        j = 0
        while j*j <= n:
            if i*i - j*j == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5)) # True

# Solution 4
import math
def dif_Square(n):
    for i in range(0, int(math.sqrt(n))+1):
        j = 0
        while j <= i:
            if i*i - j*j == n:
                return True
            j += 1
    return False

print(dif_Square(5)) # True

# Solution 5
def dif_Square(n):
    for i in range(0, int(n**0.5)+1):
        j = 0
        while j <= i:
            if i*i - j*j == n:
                return True
            j += 1
    return False

print(dif_Square(5)) # True

# Solution 6
def dif_Square(n):
    i = 0
    while i*i <= n:
        j = 0
        while j*j <= n:
            if i*i - j*j == n:
                return True
            j += 1
        i += 1
    return False

print