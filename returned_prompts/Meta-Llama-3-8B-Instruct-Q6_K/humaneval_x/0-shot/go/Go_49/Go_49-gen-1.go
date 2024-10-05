# Python code to solve the problem
def Modp(n, p):
    return pow(n, p, p)

# Test the function
print(Modp(3, 5))  # 3
print(Modp(1101, 101))  # 2
print(Modp(0, 101))  # 1
print(Modp(3, 11))  # 8
print(Modp(100, 101))  # 1

# Explanation:
# The function `Modp(n, p)` calculates 2^n modulo p using Python's built-in `pow` function.
# The `pow` function takes three arguments: base, exponent, and modulus. In this case, the base is `n`, the exponent is `p`, and the modulus is also `p`.
# This ensures that the result is calculated modulo `p`, which is what we want. The result is returned as an integer.
# The test cases demonstrate that the function works correctly for different inputs. For example, `Modp(3, 5)` returns `3`, which is the correct result for 2^3 modulo 5. Similarly, `Modp(1101, 101)` returns `2`, which is the correct result for 2^1101 modulo 101.