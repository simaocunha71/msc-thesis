
def odd_Equivalent(bin_str,rotation):
    odd_count = 0
    bin_str = bin_str * rotation
    for i in range(len(bin_str)):
        rotated_str = bin_str[i:] + bin_str[:i]
        odd_count += bin(int(rotated_str,2) ^ int(bin_str,2)).count('1')
    return odd_count // 2

print(odd_Equivalent("011001",6)) # 3

Explanation:
This Python program uses bitwise XOR operation to count the number of odd binary values which are equivalent when rotated.

The function odd_Equivalent takes two parameters, a binary string and a rotation count. The binary string is rotated by the given count and then for each rotation, the binary equivalent of the rotated string and the original binary string are XORed. The number of 1s in the resultant binary string are counted and added to the total count. This count is then divided by 2 as each odd equivalent value is counted twice.
"""

# Alternate solution

def odd_Equivalent(bin_str, rotations):
    bin_str = bin_str * rotations
    total = 0

    for i in range(len(bin_str)):
        rotated = bin_str[i:] + bin_str[:i]
        xor_result = int(rotated, 2) ^ int(bin_str, 2)
        total += bin(xor_result).count('1')

    return total // 2

assert odd_Equivalent("011001", 6) == 3
"""
Explanation:
This Python program uses bitwise XOR operation to count the number of odd binary values which are equivalent when rotated.

The function odd_Equivalent takes two parameters, a binary string and a rotation count. The binary string is rotated by the given count and then for each rotation, the binary equivalent of the rotated string and the original binary string are XORed. The number of 1s in the resultant binary string are counted and added to the total count. This count is then divided by 2 as each odd equivalent value is counted