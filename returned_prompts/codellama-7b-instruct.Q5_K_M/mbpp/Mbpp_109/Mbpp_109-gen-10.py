"""
def odd_Equivalent(binary_str,rotation_num):
    result = 0
    for i in range(rotation_num):
        temp = binary_str[1:] + binary_str[0]
        for j in range(len(temp)):
            if temp[j] == '1':
                result += 1
    return result
"""

