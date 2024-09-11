def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n.bit_length()+ (n & (n-1) == 0))


# Tests
assert next_power_of_2(0) == 1
assert next_power_of_2(1) == 2
assert next_power_of_2(2) == 4
assert next_power_of_2(3) == 4
assert next_power_of_2(4) == 8
assert next_power_of_2(5) == 8
assert next_power_of_2(6) == 8


"""
"""

def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n.bit_length() + (n & (n-1) == 0))

# Tests
assert next_power_of_2(0) == 1
assert next_power_of_2(1) == 2
assert next_power_of_2(2) == 4
assert next_power_of_2(3) == 4
assert next_power_of_2(4) == 8
assert next_power_of_2(5) == 8
assert next_power_of_2(6) == 8


"""
"""

def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n.bit_length() + (n & (n-1) == 0))

# Tests
assert next_power_of_2(0) == 1
assert next_power_of_2(1) == 2
assert next_power_of_2(2) == 4
assert next_power_of_2(3) == 4
assert next_power_of_2(4) == 8
assert next_power_of_2(5) == 8
assert next_power_of_2(6) == 8


"""
"""