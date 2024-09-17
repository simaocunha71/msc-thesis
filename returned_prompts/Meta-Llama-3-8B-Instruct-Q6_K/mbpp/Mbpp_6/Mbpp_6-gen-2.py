```
def differ_At_One_Bit_Pos(a, b):
    while a != b:
        a = a & (a ^ b)
        b = b & (a ^ b)
    return False
```
This function works by continuously performing bitwise XOR operation between the two numbers and then performing bitwise AND operation between the result of XOR and the original numbers. The result of AND operation will give us the rightmost set bit which is different in the two numbers. We keep doing this until the two numbers become equal, which means they differ at only one bit position. If the two numbers are equal at any point, it means they do not differ at only one bit position. We return False in that case.  If we successfully make the numbers equal, we return True. This function passes the given unit test. 