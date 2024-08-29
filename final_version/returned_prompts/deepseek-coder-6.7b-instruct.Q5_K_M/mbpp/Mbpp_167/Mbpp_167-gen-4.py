def next_power_of_2(n):
    if (n <= 0):
        return 1
    if (n & (n - 1)):
        return 2 * (n.bit_length() + 1)
    else:
        return n

print(next_power_of_2(0))
print(next_power_of_2(1))
print(next_power_of_2(2))
print(next_power_of_2(3))
print(next_power_of_2(8))
print(next_power_of_2(15))
print(next_power_of_2(16))

"""
Explanation:
The bitwise AND of n and n-1 will be 0 for all powers of 2.
For example, if n is 16 (which is 2^4), n & (n-1) will be 0.
Therefore, 2*(n.bit_length() + 1) will return the next power of 2.

If n is not a power of 2, then n & (n-1) will not be 0.
In this case, n will be returned.
"""

"""
Test Cases:
next_power_of_2(0) == 1
next_power_of_2(1) == 1
next_power_of_2(2) == 2
next_power_of_2(3) == 4
next_power_of_2(8) == 8
next_power_of_2(15) == 16
next_power_of_2(16) == 16
"""

# Solution 2:
"""
def next_power_of_2(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n >>= 1
        count += 1
    return 1 << count
"""

"""
Test Cases:
next_power_of_2(0) == 1
next_power_of_2(1) == 1
next_power_of_2(2) == 2
next_power