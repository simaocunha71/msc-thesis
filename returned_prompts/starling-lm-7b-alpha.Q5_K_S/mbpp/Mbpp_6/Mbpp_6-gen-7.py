
def differ_At_One_Bit_Pos(n1, n2):
    if n1 == n2:
        return False
    n1 = format(n1, 'b')
    n2 = format(n2, 'b')
    if len(n1) != len(n2):
        return False
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            return True
    return False


