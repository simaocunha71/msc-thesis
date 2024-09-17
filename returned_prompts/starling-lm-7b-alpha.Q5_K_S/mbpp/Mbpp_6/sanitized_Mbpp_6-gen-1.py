def differ_At_One_Bit_Pos(x,y):
    xx = bin(x)
    yy = bin(y)
    if len(set(xx[2:]) & set(yy[2:]))!=1:
        return False
    return True