
def next_power_of_2(n: int) -> int:
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()

print(next_power_of_2(0))

"""
Explanation:

The bit_length() function returns the number of bits needed to represent the number in binary, which is equivalent to the number of bits in the smallest power of 2 that is greater than or equal to the number.

For example, if n = 0:
    0 - 1 bit
    1 - 2 bits
    2 - 4 bits
    3 - 8 bits
    ...
So, 0 needs 1 bit.
"""

# Test cases:
assert next_power_of_2(0) == 1
assert next_power_of_2(1) == 2
assert next_power_of_2(3) == 4
assert next_power_of_2(7) == 8
assert next_power_of_2(8) == 8
assert next_power_of_2(9) == 16
assert next_power_of_2(1023) == 1024
assert next_power_of_2(1024) == 1024
assert next_power_of_2(1025) == 2048
assert next_power_of_2(2047) == 2048
assert next_power_of_2(2048) == 2048
assert next_power_of_2(2049) == 4096
assert next_power_of_2(1000000) == 1048576
assert next_power_of_2(1234567) == 134217728
assert next_power_of_2(16384) == 16384
assert next_power_of_2(999999) == 1048576
assert next_power_of_2(123456) == 134217728
assert