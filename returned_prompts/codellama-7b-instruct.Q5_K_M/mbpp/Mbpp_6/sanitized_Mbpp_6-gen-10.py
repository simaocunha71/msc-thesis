def differ_At_One_Bit_Pos(a,b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    if len(bin_a) != len(bin_b):
        return False
    count = 0
    for i in range(len(bin_a)):
        if bin_a[i] != bin_b[i]:
            count += 1
            if count > 1:
                return False
    return True