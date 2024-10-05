
    # first sort the inputs to make sure c is the longest side
    a, b, c = sorted([a, b, c])

    # then use the Pythagorean theorem to check if c^2 is equal to a^2 + b^2
    return c**2 == a**2 + b**2

# testing
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(3, 6, 8))  # False

Explanation:

This solution works by first sorting the inputs to ensure that the longest side is stored in c. It then uses the Pythagorean theorem, which states that in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. We can use this theorem to check if the triangle is right-angled.

Here is the explanation for the code:

- We first sort the inputs to ensure that c is the longest side. This is because the Pythagorean theorem states that the square of the hypotenuse (c) is equal to the sum of the squares of the other two sides (a and b). If a and b are not the longest sides, we could still use the theorem, but it would be less useful.

- We then use the Pythagorean theorem to check if the square of the longest side (c) is equal to the sum of the squares of the other two sides (a and b). If this is true, then a, b, and c form a right-angled triangle, so we return True. Otherwise, we return False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Given a string of space-separated numbers, return the highest and lowest number as a tuple.Example