
To determine if a triangle is right angled, we need to check if the square of one of the sides is equal to the sum of the squares of the other two sides.

In other words, we need to check if a^2 + b^2 = c^2

Here's how you can do it in Python:

```python
def rightAngleTriangle(a, b, c):
    return a**2 + b**2 == c**2
```

In the above code, we use the `**` operator to calculate the square of a number. The `==` operator is used to check if two values are equal. 

For example, if you call `rightAngleTriangle(3, 4, 5)`, it will return `True` because 3^2 + 4^2 equals 5^2. 

On the other hand, if you call `rightAngleTriangle(1, 2, 3)`, it will return `False` because 1^2 + 2^2 does not equal 3^2. 

I hope this helps! Let me know if you have any more questions.

Here's the code explanation:

The `rightAngleTriangle` function takes three parameters `a`, `b`, and `c`, which represent the lengths of the three sides of the triangle. 

Inside the function, we use the `**` operator to calculate the square of each side. The `**` operator raises a number to the power of 2. 

We then compare the sum of the squares of sides `a` and `b` with the square of side `c` using the `==` operator. If the two sides are equal, the function returns `True`, indicating that the triangle is right angled. Otherwise, it returns `False`.

You can use this function to check if a triangle is right angled by calling it with the lengths of its sides as arguments.

For example, `rightAngleTriangle(3, 4, 5)` will return `True` because the square of side 3 (3^2) plus the square of side 4 (4^2) equals the square of side 5 (5^2). 

On the other hand, `rightAngleTriangle(1, 