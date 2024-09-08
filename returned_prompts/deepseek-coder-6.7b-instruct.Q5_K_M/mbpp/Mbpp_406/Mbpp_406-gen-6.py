"""
The parity of a given number can be determined by checking the remainder of the division of the number by 2. 
If the remainder is 0, the number is even and if the remainder is 1, the number is odd.
"""

def find_Parity(n):
    if n % 2 == 1:
        return True
    else:
        return False

# Test Cases
assert find_Parity(12) == False
assert find_Parity(11) == True
assert find_Parity(0) == False
assert find_Parity(2) == False
assert find_Parity(3) == True
print('All Test Cases Passed')

