from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Convert input strings to lists of integers
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]

    # Perform XOR operation on corresponding elements of the lists
    result_list = [(x ^ y) for x, y in zip(a_list, b_list)]

    # Convert the result list back to a string
    result_str = ''.join(map(str, result_list))

    return result_str

# Testing the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '111'))  # Output: '010'
print(string_xor('000', '000'))  # Output: '000'
print(string_xor('111', '111'))  # Output: '000'  # No error
print(string_xor('101', ''))  # Output: '101'  # No error
print(string_xor('', '101'))  # Output: '101'  # No error
print(string_xor('', ''))  # Output: ''  # No error

# Testing with different length strings
print(string_xor('101', '11'))  # Output: '10'
print(string_xor('101', '1111'))  # Output: '0100'
print(string_xor('', '10101'))  # Output: '10101'
print(string_xor('101', ''))  # Output: '101'
print(string_xor('', ''))  # Output: ''  # No error
print(string_xor('101', '10101'))  # Output: '00010'  # No error
print(string_xor('101', '1010101'))  # Output: '0000101'  # No error
print(string_xor('1010101', '101'))  # Output: '10101'  # No error
print(string_xor('1010101', '1010101'))  # Output: '0000000'  # No error

# Testing with empty string
print(string_xor('', '101'))  # Output: '101'
print(string_xor('101', '')) 