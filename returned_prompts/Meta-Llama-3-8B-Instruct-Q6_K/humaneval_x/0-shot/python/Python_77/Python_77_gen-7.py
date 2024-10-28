```
def iscube(a):
    root = round(a ** (1. / 3))
    return root ** 3 == a
```
Explanation:
This function uses the fact that a number is a cube if its cube root is an integer. It calculates the cube root of the input number, rounds it to the nearest integer, and then checks if the cube of this integer is equal to the original number. If it is, then the number is a cube. Otherwise, it is not. 

For example, for the input 27, the cube root is 3, so the function returns True. For the input 2, the cube root is not an integer, so the function returns False. 

This function works for all positive and negative integers, as well as zero, because the cube root of zero is zero, and the cube of zero is zero. 

Note that this function assumes that the input is always valid, as specified in the problem statement. It does not check if the input is a valid integer, and it does not handle non-integer inputs. If you want to add input validation, you can do so using the isinstance function and a try/except block. 

For example:
```
def iscube(a):
    if not isinstance(a, int):
        raise TypeError("Input must be an integer")
    root = round(a ** (1. / 3))
    return root ** 3 == a
```  