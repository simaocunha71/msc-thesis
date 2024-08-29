def next_Perfect_Square(n):
    import math
    root = math.sqrt(n)
    if root != int(root):
        root = int(root) + 1
    return root * root

print(next_Perfect_Square(35))  # 36

"""
Explanation:
In this function, we first calculate the square root of the given number. If the square root is not a whole number, we round it up to the nearest whole number. 
Then we square the root (since a square number has a root that is equal to the square root of itself) and return the result. 
This way we find the next perfect square that is greater than the given number.
"""
<jupyter_output>
36
<jupyter_text>
Question 2
<jupyter_code>
