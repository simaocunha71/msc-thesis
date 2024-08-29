"""
To solve this problem, we can use the formula for the nth decagonal number.

The formula for the nth decagonal number is given by:

    Dn = n*(7*n - 5)/2

Here is a Python function that implements this formula:
"""

def is_num_decagonal(n):
    return n*(7*n - 5)//2

# Test
assert is_num_decagonal(3) == 27
assert is_num_decagonal(10) == 917
assert is_num_decagonal(1) == 1
assert is_num_decagonal(2) == 9
assert is_num_decagonal(16) == 3859
assert is_num_decagonal(7) == 493
assert is_num_decagonal(5) == 305
assert is_num_decagonal(8) == 547
assert is_num_decagonal(6) == 345
assert is_num_decagonal(9) == 633
assert is_num_decagonal(12) == 819
assert is_num_decagonal(13) == 927
assert is_num_decagonal(17) == 4299
assert is_num_decagonal(14) == 1035
assert is_num_decagonal(15) == 1245
assert is_num_decagonal(18) == 4753
assert is_num_decagonal(19) == 5165
assert is_num_decagonal(20) == 5605
assert is_num_decagonal(21) == 6073
assert is_num_decagonal(22) == 6569
assert is_num_decagonal(23) == 7093
assert is_num_decagonal(24) == 7645
assert is_num_decagonal(25) == 8225
"""
End of script.
"""

print("All test cases pass")

#test_is_num_decagonal.py
import unittest
from is_num_decagonal import is_num_dec