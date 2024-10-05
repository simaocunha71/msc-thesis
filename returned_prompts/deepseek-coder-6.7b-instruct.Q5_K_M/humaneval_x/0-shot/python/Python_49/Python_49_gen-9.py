

def modp(n: int, p: int):
    if n == 0:
        return 1 % p
    else:
        return (2 ** n) % p

print(modp(3, 5))
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))


# 3
# 2
# 1
# 8
# 1

Explanation:

The function modp calculates the remainder of the division of 2^n by p. If n is 0, the result will be 1 (mod p), because any number raised to the power of 0 is 1.
The function takes two integer arguments: n and p. It returns the remainder of 2^n divided by p.
"""

# Task 2

"""
