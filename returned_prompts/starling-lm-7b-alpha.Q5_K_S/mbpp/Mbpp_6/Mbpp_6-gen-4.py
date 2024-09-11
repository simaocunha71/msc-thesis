"""
def differ_At_One_Bit_Pos(num1, num2):
    if (num1 ^ num2) & (num1 | num2) == 0:
        return True
    else:
        return False
"""

def differ_At_One_Bit_Pos(num1, num2):
    return bin(num1 ^ num2).count('1') == 1


# assert differ_At_One_Bit_Pos(13, 9) == True
# assert differ_At_One_Bit_Pos(13, 8) == False
# assert differ_At_One_Bit_Pos(1, 2) == True
# assert differ_At_One_Bit_Pos(1, 3) == False

# 10011
# 1001

def diff_one(n1, n2):
    n1, n2 = bin(n1)[2:], bin(n2)[2:]
    if len(n1) > len(n2):
        return diff_one(n2, n1)
    if n1 == n2[:len(n1)]:
        return False
    else:
        return True

# assert diff_one(13, 9) == True
# assert diff_one(13, 8) == False
# assert diff_one(1, 2) == True
# assert diff_one(1, 3) == False


"""
The XOR of the two numbers is zero, and the OR is not zero. If the XOR is zero, it means the two numbers are equal,
which is a contradiction to the condition that the XOR is not zero.
"""

















































































































