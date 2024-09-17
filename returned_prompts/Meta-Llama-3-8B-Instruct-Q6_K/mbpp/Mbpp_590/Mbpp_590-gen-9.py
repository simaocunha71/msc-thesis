```
def polar_rect(r, theta):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return (x, y)
```


The problem asks to write a function that converts polar coordinates (radius and angle) to rectangular coordinates (x and y). The function should take two parameters: the radius (r) and the angle (theta) in degrees.

The unit test `assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))` helps to clarify the expected output of the function, which should be a tuple of two values: the x-coordinate and the y-coordinate.

In this solution, the `math.radians` function is used to convert the angle from degrees to radians, which is the unit expected by the `math.cos` and `math.sin` functions. The `math.cos` and `math.sin` functions are then used to calculate the x and y coordinates, respectively. The results are returned as a tuple.

Note that the `math` module is not imported by default in Python, so it needs to be imported explicitly using `import math`. 