def differ_At_One_Bit_Pos(a, b):
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]
    if len(a_bin) > len(b_bin):
        a_bin, b_bin = b_bin, a_bin
    for i in range(len(a_bin)):
        if a_bin[i] != b_bin[i]:
            return True
    return False