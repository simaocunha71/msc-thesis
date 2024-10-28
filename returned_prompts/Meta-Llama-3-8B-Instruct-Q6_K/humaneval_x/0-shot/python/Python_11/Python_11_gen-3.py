from typing import List

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    result = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '0' and b[i] == '0':
            result += '0'
        else:
            result += '1'
    return result
# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
# Test for different lengths:
print(string_xor('101', '1110'))  # Raises ValueError
# Test for invalid input:
print(string_xor('abc', '110'))  # Raises ValueError
# Test for empty strings:
print(string_xor('', ''))  # Output: ''
print(string_xor('101', ''))  # Raises ValueError
print(string_xor('', '110'))  # Raises ValueError
# Test for single-character strings:
print(string_xor('1', '0'))  # Output: '1'
print(string_xor('0', '1'))  # Output: '1'
print(string_xor('1', '1'))  # Output: '0'
print(string_xor('0', '0'))  # Output: '0'
# Test for identical strings:
print(string_xor('101', '101'))  # Output: '000'
# Test for all-1 or all-0 strings:
print(string_xor('111', '111'))  # Output: '000'
print(string_xor('000', '000'))  # Output: '000'  # Test for different lengths:
print(string_xor('101', '1110'))  # Raises ValueError
# Test for invalid input:
print(string_xor('abc', '110'))  # Raises ValueError
# Test for empty strings:
print(string_xor('', ''))  # Output: ''
print(string_xor('101', ''))  # Raises ValueError
print(string_xor('', '110'))  # Raises ValueError
# Test for single-character strings:
print(string_xor('1', '0'))  # Output: '1'
print(string_xor('0', '1'))  # Output: '1'
print(string_xor('1',