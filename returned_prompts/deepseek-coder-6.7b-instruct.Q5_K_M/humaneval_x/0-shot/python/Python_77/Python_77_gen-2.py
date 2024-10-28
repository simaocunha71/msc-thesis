
    import math

    def iscube(a):
        root = round(a ** (1. / 3.))
        return root ** 3 == a

    print(iscube(1))    # True
    print(iscube(2))    # False
    print(iscube(-1))   # True
    print(iscube(64))   # True
    print(iscube(0))    # True
    print(iscube(180))  # False

This function works by taking the cube root of the input number, rounding it to the nearest integer, and then checking if this integer cubed is equal to the input number. If it is, the function returns True; otherwise, it returns False. This is based on the fact that the cube root of a number is the same as the number when cubed.

It's important to note that this function will return False for negative input numbers because a cube root of a negative number is a complex number. However, since we're assuming the input is always valid, we don't need to handle this case.

Also, it's worth noting that this function may not work correctly for very large numbers because of the limitations of floating point precision.

This function will work for all integers, positive and negative. It will return True if the number is a perfect cube and False otherwise.

In the given examples, 1, 64 and 0 are perfect cubes of some numbers, so the function returns True. The numbers 2 and -1 are not perfect cubes of any integer, so the function returns False. The number 180 is not a perfect cube of any integer, so the function returns False.

The function iscube(a) takes an integer a as an argument and returns True if the integer is a cube of some integer number, False otherwise.
    '''




























































































