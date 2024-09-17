You can solve this problem by using bitwise operations. The idea is to XOR the two numbers and count the number of bits in the result. If the count is 1, then the two numbers differ at one bit position.

Here is the Python function that implements this idea:
```
def differ_At_One_Bit_Pos(a, b):
    return bin(a^b).count('1') == 1
```
This function works by first calculating the XOR of the two numbers `a` and `b` using the `^` operator. The result is a number where each bit is 1 if the corresponding bits in `a` and `b` are different. The `bin` function is used to convert this number to a binary string, and the `count` method is used to count the number of 1's in this string. If the count is 1, then the two numbers differ at one bit position, and the function returns `True`. Otherwise, it returns `False`.

The unit test `assert differ_At_One_Bit_Pos(13,9) == True` passes because the binary representations of 13 and 9 are `1101` and `1001`, respectively, and they differ at one bit position (the third bit). The function correctly returns `True` for this input.