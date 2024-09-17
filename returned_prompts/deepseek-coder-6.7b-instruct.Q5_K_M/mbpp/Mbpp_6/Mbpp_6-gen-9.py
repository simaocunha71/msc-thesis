
def differ_At_One_Bit_Pos(x, y):
    return bin(x ^ y).count('1') == 1
"""
In this function, we are XORing the two numbers and converting the result to binary. Then we count the number of 1s in the result. If the count is 1, it means that exactly one bit differs in x and y, so the function returns True. Otherwise, it returns False.
"""

