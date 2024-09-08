
def find_Parity(n):
    # convert the number to binary
    bin_n = bin(n)[2:]
    # count the number of ones in the binary representation
    count = bin_n.count('1')
    # if count is odd, return True, else return False
    return count % 2 != 0

print(find_Parity(12)) # False

"""
Here, we convert the given number to binary, count the number of 1s in the binary representation and check if the count is odd or not.
"""

# Alternate solution

def find_Parity(n):
    return bin(n).count('1') % 2 != 0

print(find_Parity(12)) # False

"""
In this alternate solution, we directly convert the given number to binary and count the number of 1s in the binary representation. Then we check if the count is odd or not.
"""
<jupyter_output>
False
False
<jupyter_text>
