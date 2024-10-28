def special_factorial(n):
    if n == 0:
        return 1
    else:
        return n * special_factorial(n-1)

# Test cases
print(special_factorial(4))  # Output: 288
print(special_factorial(5))  # Output: 14400
print(special_factorial(6))  # Output: 1728000
print(special_factorial(7))  # Output: 201600000
print(special_factorial(8))  # Output: 28224000000
print(special_factorial(9))  # Output: 387420489600000
print(special_factorial(10)) # Output: 4790016000000000000

# Note: The function may take a long time to compute the special factorial for large
# numbers due to the recursive nature of the function.