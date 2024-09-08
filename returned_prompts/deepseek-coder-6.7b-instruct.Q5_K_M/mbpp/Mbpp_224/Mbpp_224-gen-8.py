def count_Set_Bits(n):
    return bin(n).count('1')

print(count_Set_Bits(2)) # Should print 1

"""
Explanation:
The bin function converts the given integer into binary and returns a string representation. The count function counts the number of occurrences of the specified value ('1') in the string.
"""


# 2.

