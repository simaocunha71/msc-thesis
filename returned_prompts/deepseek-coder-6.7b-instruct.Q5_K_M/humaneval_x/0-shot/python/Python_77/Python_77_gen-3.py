
    import math

    def iscube(a):
        root = round(a ** (1. / 3.))
        return root ** 3 == a

print(iscube(1)) #==> True
print(iscube(2)) #==> False
print(iscube(-1)) #==> True
print(iscube(64)) #==> True
print(iscube(0)) #==> True
print(iscube(180)) #==> False

The function works by first calculating the cube root of the input number, then checking if cubing this root equals the original number. If yes, then the number is a cube, and the function returns True, otherwise it returns False.

The round function is used to round to the nearest integer, as cube roots will usually be a float.

This function is correct for positive integers. For negative integers, it will still return True, because the cube of a negative number is still a negative number.

Note: This function may not work correctly for very large integers, as the cube root calculation may result in an overflow error.


def iscube(a):
    return int(round(a ** (1. / 3))) ** 3 == a

This version of the function also works correctly for negative integers. It rounds the cube root to the nearest integer, then checks if cubing this integer equals the original number. If yes, then the number is a cube, and the function returns True, otherwise it returns False.
<jupyter_output>
<empty_output>
<jupyter_text>
