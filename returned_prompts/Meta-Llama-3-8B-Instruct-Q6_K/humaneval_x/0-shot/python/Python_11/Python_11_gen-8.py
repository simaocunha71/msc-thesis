from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '0' and b[i] == '0':
            result += '0'
        else:
            result += '1'
    return result
#test the function
print(string_xor('010', '110'))  # Should return '100'
print(string_xor('111', '000'))  # Should return '111' 
print(string_xor('000', '000'))  # Should return '000' 
print(string_xor('100', '111'))  # Should return '011'  # Should return '011'
# print(string_xor('101010', '111011'))  # Should return '010001' 
# print(string_xor('000000', '000000'))  # Should return '000000' 
# print(string_xor('111111', '111111'))  # Should return '000000'  # Should return '000000' 
# print(string_xor('101010', '101010'))  # Should return '000000' 
# print(string_xor('111111', '000000'))  # Should return '111111' 
# print(string_xor('000000', '111111'))  # Should return '111111' 
# print(string_xor('101010', '111111'))  # Should return '010101' 
# print(string_xor('000000', '101010'))  # Should return '101010' 
# print(string_xor('111111', '101010'))  # Should return '010101'  # Should return '010101' 
# print(string_xor('101010', '101010'))  # Should return '000000' 
# print(string_xor('111111', '111111'))  # Should return '000000' 
# print(string_xor('000000', '000000'))  # Should return '000000'  # Should return '000000' 
# print(string_xor('111111', '111111'))  # Should return '000000' 
# print(string_xor('000000', '000000'))  # Should return '000000' 
# print(string_xor('101010', '101010'))  # Should return '000000' 
# print(string_xor('