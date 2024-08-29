def next_Perfect_Square(n):
    import math
    root = math.sqrt(n)
    if root != int(root):
        root = int(root) + 1
    return root * root

print(next_Perfect_Square(35))

# Alternate Solution
def next_Perfect_Square(n):
    i = n + 1
    while True:
        root = i ** 0.5
        if root == int(root):
            return i
        i += 1

print(next_Perfect_Square(35))


# Alternate Solution using built-in Python math module
import math

def next_Perfect_Square(n):
    root = math.sqrt(n)
    if root.is_integer():
        root += 1
    else:
        root = int(root) + 1
    return root ** 2

print(next_Perfect_Square(35))

"""
The first solution uses the built-in math module to compute the square root of n and then checks if the root is an integer. If it is not, it increments the root by 1 and squares it to get the next perfect square.

The second solution uses a while loop to increment i until it finds a number whose square root is an integer. It then returns the square of that number.

The third solution is similar to the first solution but uses the math.sqrt function to get the square root of n and the is_integer method to check if the root is an integer.
"""

# All three solutions return 36 which is the next perfect square of 35.
<jupyter_output>
36
36
36
<jupyter_text>
7. Write a Python program that accepts a list of integers and calculates the difference between the largest and smallest values in the list.assert list_diff([1, 2, 3, 4, 5]) == 4assert list_diff([5, 1, 9, 3, 7]) == 8
<jupyter_code>
def list_diff(lst):
    return max(lst) - min(lst)

