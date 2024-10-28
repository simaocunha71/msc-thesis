

def modp(n: int, p: int) -> int:
    return (2**n) % p

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1

# Alternative solution using built-in pow function
def modp(n: int, p: int) -> int:
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1


This solution uses the built-in `pow` function which allows for an optional third argument to calculate the modulus of the power operation.
'''

# Alternative solution using built-in pow function
def modp(n: int, p: int) -> int:
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
<jupyter_output>
3
2
1
8
1
<jupyter_text>
Problem 2:
<jupyter_code>
'''
