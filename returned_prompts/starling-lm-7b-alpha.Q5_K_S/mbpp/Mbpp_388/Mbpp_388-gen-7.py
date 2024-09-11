def highest_Power_of_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(32):
        if 2 ** i <= n:
            return 2 ** i

# Testing
assert(highest_Power_of_2(10) == 8)










"""
Correct Solution:
"""
def highest_Power_of_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 0
    while True:
        if 2 ** i <= n:
            return 2 ** i
        i += 1

# Testing
assert(highest_Power_of_2(10) == 8)
```