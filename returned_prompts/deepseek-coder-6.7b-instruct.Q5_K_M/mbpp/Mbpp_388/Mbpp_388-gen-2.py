def highest_Power_of_2(n):
    i = 0
    while 2 ** i <= n:
        i += 1
    return 2 ** (i - 1)

print(highest_Power_of_2(10))

# another way to solve this problem is by using bitwise operation
def highest_Power_of_2(n):
    i = 0
    while (1 << i) <= n:
        i += 1
    return (1 << (i - 1))

print(highest_Power_of_2(10))

# or even simpler
def highest_Power_of_2(n):
    i = 1
    while i <= n:
        i *= 2
    return i // 2

print(highest_Power_of_2(10))

"""
The function works by starting at power 0 and incrementing the power until 2 to that power is greater than n. The function then returns 2 to the power before this point (i.e., the highest power of 2 that is less than or equal to n). 

Note: The bitwise shift operation is used in the second method. The left shift operator "<<" shifts the bits of the number to the left by the specified amount. So (1 << i) is equivalent to 2 ** i.
"""

# another way to solve this problem is by using binary operation
def highest_Power_of_2(n):
    i = 0
    while (1 << i) <= n:
        i += 1
    return (1 << (i - 1))

print(highest_Power_of_2(10))

# or even simpler
def highest_Power_of_2(n):
    i = 1
    while i <= n:
        i *= 2
    return i // 2

print(highest_Power_of_2(10))

# The function works by starting at power 0 and incrementing the power until 2 to that power is greater than n. The function then returns 2 to the power before this point (i.e., the highest power of 2 that is less than or equal to n). 

# Note: The bitwise