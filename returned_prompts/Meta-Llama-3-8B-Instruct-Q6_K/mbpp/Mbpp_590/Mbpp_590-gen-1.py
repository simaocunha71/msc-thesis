```
def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
```


This function takes polar coordinates (r, theta) as input and returns the corresponding rectangular coordinates (x, y).

The formula to convert polar coordinates to rectangular coordinates is: x = r * cos(theta), y = r * sin(theta).

The unit test `assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))` is used to verify the correctness of the function. The function should return the correct rectangular coordinates for the given polar coordinates.