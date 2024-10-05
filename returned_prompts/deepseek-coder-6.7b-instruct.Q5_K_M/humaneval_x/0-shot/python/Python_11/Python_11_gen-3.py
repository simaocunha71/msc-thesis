from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_result = []
    for i in range(len(a)):
        xor_result.append(str(int(a[i]) ^ int(b[i])))
    return ''.join(xor_result)


print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
print(string_xor('100', '001'))  # Output: '101'
print(string_xor('1111', '1001'))  # Output: '0110'


Explanation:
We are given two binary strings a and b of the same length n. We need to perform a binary XOR operation on these two strings and return the resultant string.

A binary XOR operation between two bits returns 1 if the two bits are different. If the two bits are the same, it returns 0.

To solve this problem, we iterate over each character in the given strings a and b at the same index. We convert the characters to integers using the int() function, perform the XOR operation using the ^ operator, and then append the result to the list xor_result. Finally, we join the elements of xor_result to form the final string and return it.

The time complexity of this solution is O(n), where n is the length of the input strings. The space complexity is also O(n) as we are storing the result in a list.

This solution assumes that the input strings a and b are of the same length. If they can be of different lengths, we would need to first pad the shorter string with zeros to make them of equal length before performing the XOR operation.

This solution also assumes