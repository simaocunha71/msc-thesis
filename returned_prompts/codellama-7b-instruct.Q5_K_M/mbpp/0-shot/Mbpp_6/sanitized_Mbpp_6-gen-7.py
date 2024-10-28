def differ_At_One_Bit_Pos(a,b):
    bin_a = bin(a)
    bin_b = bin(b)
    bit_pos = []
    for i in range(len(bin_a)):
        if bin_a[i] != bin_b[i]:
            bit_pos.append(i)
    return len(bit_pos) == 1