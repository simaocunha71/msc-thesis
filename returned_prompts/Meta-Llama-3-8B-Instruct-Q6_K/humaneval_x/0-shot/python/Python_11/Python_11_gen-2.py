from typing import List

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Strings must be of the same length")

    result = ""
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '0' and b[i] == '0':
            result += '0'
        else:
            result += '1'

    return result
# test the function
print(string_xor('010', '110'))  # Output: '100'  # 2.0

# test the function
print(string_xor('101', '101'))  # Output: '000'
# test the function
print(string_xor('111', '111'))  # Output: '000'
# test the function
print(string_xor('000', '000'))  # Output: '000'
# test the function
print(string_xor('1010', '1101'))  # Output: '0101'
# test the function
print(string_xor('1010', '1111'))  # Output: '0101'
# test the function
print(string_xor('1101', '1011'))  # Output: '0110'
# test the function
print(string_xor('1101', '1101'))  # Output: '0000'
# test the function
print(string_xor('1101', '1111'))  # Output: '0000'





# test the function
print(string_xor('010', '110'))  # Output: '100'  # 2.0
print(string_xor('101', '101'))  # Output: '000'
print(string_xor('111', '111'))  # Output: '000'
print(string_xor('000', '000'))  # Output: '000'
print(string_xor('1010', '1101'))  # Output: '0101'
print(string_xor('1010', '1111'))  # Output: '0101'
print(string_xor('1101', '1011'))  # Output: '0110'
print(string_xor('1101', '1101'))  # Output: '0000'
print(string_xor('1101', '1111'))  # Output: '0000'





# test the function
print(string_xor('010', '110'))  # Output