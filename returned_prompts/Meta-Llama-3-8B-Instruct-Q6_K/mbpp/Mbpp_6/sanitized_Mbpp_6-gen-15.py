def differ_At_One_Bit_Pos(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    if len(bin_a) > len(bin_b):
        bin_a, bin_b = bin_b, bin_a
    for i in range(len(bin_a)):
        if bin_a[i] != bin_b[i]:
            if i == len(bin_a) - 1:
                return True
            if bin_a[i+1] != bin_b[i+1]:
                return False
    return True