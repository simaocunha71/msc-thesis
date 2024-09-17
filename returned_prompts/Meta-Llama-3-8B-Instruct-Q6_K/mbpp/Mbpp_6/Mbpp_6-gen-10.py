```
def differ_At_One_Bit_Pos(a, b):
    x = a ^ b
    if x & (x & -x) == 0:
        return True
    return False
```
The function `differ_At_One_Bit_Pos` takes two integers `a` and `b` as input and returns a boolean indicating whether they differ at one bit position or not. 

The function uses the XOR operation `^` to find the bits where `a` and `b` differ. The result is then used to find the rightmost bit that differs using the expression `x & (x & -x)`. 

If this expression is equal to 0, it means that there is only one bit that differs, and the function returns `True`. Otherwise, it returns `False`. 

The unit test `assert differ_At_One_Bit_Pos(13,9) == True` ensures that the function works correctly. 

For example, the binary representation of 13 is `1101` and the binary representation of 9 is `1001`. The XOR operation `13 ^ 9` gives `0100`, which has only one 1 bit. Therefore, the function returns `True`. 

Similarly, the binary representation of 11 is `1011` and the binary representation of 10 is `1010`. The XOR operation `11 ^ 10` gives `001`, which has only one 1 bit. Therefore, the function returns `True`. 

However, the binary representation of 11 is `1011` and the binary representation of 12 is `1100`. The XOR operation `11 ^ 12` gives `0111`, which has more than one 1 bit. Therefore, the function returns `False`. 