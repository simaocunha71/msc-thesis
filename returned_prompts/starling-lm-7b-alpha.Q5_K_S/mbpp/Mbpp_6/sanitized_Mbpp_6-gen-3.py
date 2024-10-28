def differ_At_One_Bit_Pos(a,b):
    a = bin(a)
    a = a[2:]
    b = bin(b)
    b = b[2:]
    if len(a) != len(b):
        return False
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False