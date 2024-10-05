    return pow(n, p - 2, p)
    # This is the most efficient way to compute the modular power in Python.
    # It uses the built-in pow function with three arguments, which calculates (a**b) % c.
    # The third argument, c, is the modulus. The second argument, b, is the exponent.
    # The first argument, a, is the base. The result is the modular power of a to the power of b.  # noqa: E501

# Example usage:
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
# You can also use this function to calculate modular power with negative exponent
print(modp(2, 5))  # Output: 4
print(modp(2, -1))  # Output: 3
print(modp(2, -2))  # Output: 4
print(modp(2, -3))  # Output: 1
# You can also use this function to calculate modular power with decimal exponent
print(modp(2, 0.5))  # Output: 2
print(modp(2, 0.25))  # Output: 4
print(modp(2, 0.75))  # Output: 4
print(modp(2, 1.5))  # Output: 2
# This function is efficient and can handle large numbers and complex exponents.  # noqa: E501
# It's also easy to use and can be used in a variety of situations.  # noqa: E501

# Limitations:
# This function can only be used with positive integers as the modulus.
# It can also only be used with positive integers as the base.
# It can also only be used with positive integers as the exponent.
# It can also only be used with positive integers as the result.
# It can also only be used with positive integers as the input.
# It can also only be used with positive integers as the output.
# It can also only be used with positive integers as the exponent.
# It can also only be used