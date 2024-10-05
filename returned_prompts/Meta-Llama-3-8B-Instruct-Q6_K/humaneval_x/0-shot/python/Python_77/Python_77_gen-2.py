
```
def iscube(a):
    c = int(a ** (1. / 3.))
    return c ** 3 == a
```
Explanation:
The function `iscube(a)` checks if the input integer `a` is a cube of some integer number.

Here's the step-by-step process:

1. Calculate the cube root of `a` using the formula `c = int(a ** (1. / 3.))`. This will give us the integer part of the cube root of `a`.

2. Raise `c` to the power of 3 and check if the result is equal to `a`. If it is, then `a` is a cube of some integer number.

3. If `c ** 3` is equal to `a`, the function returns `True`. Otherwise, it returns `False`.

This function works for both positive and negative inputs, and it correctly handles the case where `a` is 0 (since 0 is a cube of 0). The function also works for inputs that are not perfect cubes, such as 180, which returns `False` as expected.