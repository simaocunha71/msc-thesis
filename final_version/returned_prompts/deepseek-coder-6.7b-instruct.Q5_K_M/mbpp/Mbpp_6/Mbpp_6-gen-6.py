"""
def differ_At_One_Bit_Pos(x,y):
    bin_x = bin(x)[2:]
    bin_y = bin(y)[2:]
    if abs(len(bin_x) - len(bin_y)) > 1:
        return False
    elif len(bin_x) == len(bin_y):
        return sum([i != j for i, j in zip(bin_x, bin_y)]) == 1
    else:
        longer = bin_x if len(bin_x) > len(bin_y) else bin_y
        shorter = bin_y if len(bin_y) < len(bin_x) else bin_x
        return sum([i != j for i, j in zip(longer, shorter)]) == 1

assert differ_At_One_Bit_Pos(13,9) == True
"""

