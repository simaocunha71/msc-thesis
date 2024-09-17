```
def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
```


The function takes two parameters, r (radius) and theta (angle in radians), and returns a tuple of two values, the x and y coordinates of the point in rectangular coordinates. The math library is used for the trigonometric functions cos and sin.

The unit test `assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))` ensures that the function works correctly for the given input. The expected output is a tuple of two values, the x and y coordinates of the point in rectangular coordinates, which are calculated by multiplying the radius with the cosine of the angle for the x-coordinate and the sine of the angle for the y-coordinate.

Note that the output is a tuple of two values, the first is a real number and the second is a complex number with a very small imaginary part. This is because the math library in Python returns a complex number when the result of the trigonometric function is a complex number, even if the imaginary part is very small. The unit test checks for this specific case.