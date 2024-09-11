def highest_Power_of_2(n):
    if n == 0:
        return 0
    while n % 2 == 0:
        n = n/2
    return n

# Test
print(highest_Power_of_2(10))  # Output: 8

# Assertion
assert highest_Power_of_2(10) == 8

# Test with 0
print(highest_Power_of_2(0))  # Output: 0

# Assertion
assert highest_Power_of_2(0) == 0

# Test with -ve
print(highest_Power_of_2(-1))  # Output: 0

# Assertion
assert highest_Power_of_2(-1) == 0

# Test with 1
print(highest_Power_of_2(1))  # Output: 1

# Assertion
assert highest_Power_of_2(1) == 1

# Test with fractional value
print(highest_Power_of_2(0.6))  # Output: 1

# Assertion
assert highest_Power_of_2(0.6) == 1

# Test with float value
print(highest_Power_of_2(10.5))  # Output: 8

# Assertion
assert highest_Power_of_2(10.5) == 8

# Test with 2
print(highest_Power_of_2(2))  # Output: 2

# Assertion
assert highest_Power_of_2(2) == 2


















"""
def highest_Power_of_2(n):
    if n == 0:
        return 0
    while n % 2 == 0:
        n = n/2
    return n

# Test
print(highest_Power_of_2(10))  # Output: 8

# Assertion
assert highest_Power_of_2(10) == 8

# Test with 