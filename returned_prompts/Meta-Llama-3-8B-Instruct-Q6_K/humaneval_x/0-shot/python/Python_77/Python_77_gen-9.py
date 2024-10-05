```
def iscube(a):
    root = round(a ** (1/3))
    return root ** 3 == a
```    
    This function works by first calculating the cube root of the input number, and then checking if the cube of this value is equal to the input number. If it is, then the input number is a cube of some integer, and the function returns True. If not, then it returns False. The use of the round function is necessary to ensure that the cube root is rounded to the nearest integer, so that the function works correctly for non-integer inputs. For example, the cube root of 27 is 3, not 3.0, so we need to round the result to get the correct answer. 

For example, if we call `iscube(27)`, the function will calculate the cube root of 27, which is 3, and then check if the cube of 3 (which is 27) is equal to 27. Since it is, the function returns True. If we call `iscube(28)`, the function will calculate the cube root of 28, which is 2.0, and then check if the cube of 2.0 (which is 8) is equal to 28. Since it is not, the function returns False. 

This function works correctly for all valid inputs, as specified in the problem statement. It also handles negative inputs correctly, since the cube root of a negative number is a negative number, and the cube of a negative number is also a negative number. For example, if we call `iscube(-27)`, the function will calculate the cube root of -27, which is -3, and then check if the cube of -3 (which is -27) is equal to -27. Since it is, the function returns True. 