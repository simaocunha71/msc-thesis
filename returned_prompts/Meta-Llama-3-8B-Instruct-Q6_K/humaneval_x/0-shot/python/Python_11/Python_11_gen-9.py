from typing import List

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Both strings must have the same length")

    result = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '0' and b[i] == '0':
            result += '0'
        else:
            result += '1'

    return result
# test
print(string_xor('010', '110'))  # '100'
print(string_xor('111', '000'))  # '111'
print(string_xor('101', '011'))  # '110'
print(string_xor('abc', 'xyz'))  # ValueError: Both strings must have the same length
print(string_xor('111', 'abc'))  # ValueError: Both strings must have the same length
# Test Case 1: Test the function with two strings of the same length
print(string_xor('1010', '1111'))  # '0101'
# Test Case 2: Test the function with two strings of different lengths
print(string_xor('1010', '111'))  # ValueError: Both strings must have the same length
# Test Case 3: Test the function with two strings of equal length but with different characters
print(string_xor('1010', '1234'))  # ValueError: Both strings must have the same length
# Test Case 4: Test the function with two strings of equal length and with the same characters
print(string_xor('1010', '1010'))  # '0000'
# Test Case 5: Test the function with two strings of equal length and with the same characters but with different lengths
print(string_xor('1010', '101'))  # ValueError: Both strings must have the same length
# Test Case 6: Test the function with two strings of different lengths
print(string_xor('1010', '123'))  # ValueError: Both strings must have the same length
# Test Case 7: Test the function with two strings of the same length and with the same characters
print(string_xor('1010', '1010'))  # '0000'
# Test Case 8: Test the function with two strings of different lengths
print(string_xor('1010', '123'))  # ValueError: Both strings must have the same length