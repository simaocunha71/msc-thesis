def highest_Power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = 1
        while i < n:
            i *= 2
        return i

# assert highest_Power_of_2(10) == 8

# print(highest_Power_of_2(10))
# print(highest_Power_of_2(1))
# print(highest_Power_of_2(0))
# print(highest_Power_of_2(100))

def highest_Power_of_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    while (n & (n - 1)) > 0:
        n &= (n - 1)
    return n

# assert highest_Power_of_2(10) == 8

# print(highest_Power_of_2(10))
# print(highest_Power_of_2(1))
# print(highest_Power_of_2(0))
# print(highest_Power_of_2(100))

"""
def highest_Power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while n != 0:
            n = n >> 1
        return n

# assert highest_Power_of_2(10) == 8

# print(highest_Power_of_2(10))
# print(highest_Power_of_2(1))
# print(highest_Power_of_2(0))
# print(highest_Power_of_2(100))
"""

"""
def highest_Power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = 1
        while