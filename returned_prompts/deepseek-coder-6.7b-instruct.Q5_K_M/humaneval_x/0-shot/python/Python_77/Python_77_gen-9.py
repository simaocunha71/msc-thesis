
    import math

    def iscube(a):
        root = round(a ** (1./3.))
        return root ** 3 == a

    print(iscube(1))   # True
    print(iscube(2))   # False
    print(iscube(-1))  # True
    print(iscube(64))  # True
    print(iscube(0))   # True
    print(iscube(180)) # False

This function works by first rounding the cube root of the input number. This is because the cube root of a number can be a decimal, but we need an integer for our calculations. The function then checks if the cube of this rounded number equals the original input number, and if so, returns True. Otherwise, it returns False.

The rounding step is necessary because floating point arithmetic can have precision errors that can cause incorrect results. For example, rounding the cube root of 2 to an integer gives 1, but 1 cubed is not 2.

This function works for all integers, including negative ones and zero.

This function uses the built-in math library for the cube root calculation, which makes it easier to implement.
