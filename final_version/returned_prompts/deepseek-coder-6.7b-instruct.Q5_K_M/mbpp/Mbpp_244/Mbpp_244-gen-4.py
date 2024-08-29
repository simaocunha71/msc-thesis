def next_Perfect_Square(n):
    import math
    root = math.sqrt(n)
    if root != int(root):
        root = int(root) + 1
    return root ** 2

print(next_Perfect_Square(35))

"""
Explanation:
In this function, we use the sqrt function from the math library to find the square root of the number. 
If the square root is not an integer, we increment it by one and return the square of the new root. 
This will give us the next perfect square greater than the input number.
"""

# Testing
assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(100) == 121
assert next_Perfect_Square(0) == 1
assert next_Perfect_Square(1) == 4
assert next_Perfect_Square(121) == 144
assert next_Perfect_Square(144) == 169
assert next_Perfect_Square(169) == 196
assert next_Perfect_Square(196) == 225
assert next_Perfect_Square(225) == 256
assert next_Perfect_Square(256) == 289
assert next_Perfect_Square(289) == 324
assert next_Perfect_Square(324) == 361
assert next_Perfect_Square(361) == 400
assert next_Perfect_Square(400) == 441
assert next_Perfect_Square(441) == 484
assert next_Perfect_Square(484) == 529
assert next_Perfect_Square(529) == 576
assert next_Perfect_Square(576) == 625
assert next_Perfect_Square(625) == 676
assert next_Perfect_Square(676) == 729
assert next_Perfect_Square(729) == 