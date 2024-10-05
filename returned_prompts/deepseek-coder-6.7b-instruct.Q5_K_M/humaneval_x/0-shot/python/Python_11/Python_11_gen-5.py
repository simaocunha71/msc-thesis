from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

print(string_xor('010', '110'))

Explanation:
The function string_xor takes in two strings a and b. It uses the built-in zip function to iterate over two strings simultaneously. For each pair of characters, it converts them to integers, performs XOR operation, and then converts the result back to string. The ''.join method combines all the resulting strings into one string.
'''

# 2.
'''
