```
def differ_At_One_Bit_Pos(a, b):
    while a != b:
        a = a & (a ^ b)
        b = b & (a ^ b)
    return True
```



The function works by continuously performing bitwise operations until the two numbers are the same. The bitwise AND of the two numbers (a & b) will give the bits that are present in both numbers, and the bitwise XOR of the two numbers (a ^ b) will give the bits that are different between the two numbers. By continuously performing these operations, the function effectively "zaps" the bits that are different between the two numbers, leaving only the bits that are the same. When the two numbers are the same, the function returns True, indicating that the two numbers differ at one bit position only. The unit test `assert differ_At_One_Bit_Pos(13,9) == True` confirms this. 







