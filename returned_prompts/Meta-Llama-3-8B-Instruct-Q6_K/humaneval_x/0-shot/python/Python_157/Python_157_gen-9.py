```
def right_angle_triangle(a, b, c):
    # Check if a^2 + b^2 = c^2
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
```

Explanation:
The Pythagorean theorem states that for a right-angled triangle, the square of the length of the hypotenuse (c) is equal to the sum of the squares of the lengths of the other two sides (a and b). This theorem can be used to determine if a triangle is right-angled or not.

In the given code, the function right_angle_triangle() takes three arguments a, b, and c representing the lengths of the three sides of a triangle. It checks if the sum of the squares of the lengths of the two sides a and b is equal to the square of the length of the hypotenuse c. If the condition is met, it returns True, indicating that the triangle is right-angled. Otherwise, it returns False. 

This function can be used to determine if a given triangle is right-angled or not. For example, right_angle_triangle(3, 4, 5) returns True because the triangle with sides 3, 4, and 5 is a right-angled triangle, while right_angle_triangle(1, 2, 3) returns False because the triangle with sides 1, 2, and 3 is not right-angled. 