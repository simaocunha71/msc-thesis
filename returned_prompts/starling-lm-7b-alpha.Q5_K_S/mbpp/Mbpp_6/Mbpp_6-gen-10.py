"""
def differ_At_One_Bit_Pos(n1, n2):
    n1 = bin(n1)[2:]
    n2 = bin(n2)[2:]
    if len(n1) != len(n2):
        return False
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            if i == 0 and (n1[i] == '1' or n2[i] == '1'):
                return False
            return True
    return False


# tests
assert differ_At_One_Bit_Pos(13, 9) == True
assert differ_At_One_Bit_Pos(10, 12) == False
"""

def differ_At_One_Bit_Pos(n1, n2):
    x = n1 ^ n2
    return (x and (x & (x - 1)) == 0)

# tests
assert differ_At_One_Bit_Pos(13, 9) == True
assert differ_At_One_Bit_Pos(10, 12) == False


def differ_At_One_Bit_Pos(n1, n2):
    return bin(n1 ^ n2).count('1') == 1

# tests
assert differ_At_One_Bit_Pos(13, 9) == True
assert differ_At_One_Bit_Pos(10, 12) == False


def differ_At_One_Bit_Pos(n1, n2):
    return bin(n1 ^ n2).count('1') == 1

# tests
assert differ_At_One_Bit_Pos(13, 9) == True
assert differ_At_One_Bit_Pos(10, 12) == False

def differ_At_One_Bit_Pos(n1, n2):
    n1 = bin(n1)[2:]
    n2 = bin(n2)[2:]
    if len(n1) != len(n2):
        return False
    for i in range(len(n1)):
