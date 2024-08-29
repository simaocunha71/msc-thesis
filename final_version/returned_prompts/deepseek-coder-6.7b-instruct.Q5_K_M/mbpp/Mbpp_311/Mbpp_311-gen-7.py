def set_left_most_unset_bit(n):
    if n & 1 == 0:
        return n | 1
    else:
        return n

print(set_left_most_unset_bit(10))  # 14

"""
Explanation:
Binary representation of 10 is 1010. Here, the left most bit is unset (0) so we set it and get 1010 (binary) which is 14 (decimal).
"""

# Python Program to clear the left most set bit

