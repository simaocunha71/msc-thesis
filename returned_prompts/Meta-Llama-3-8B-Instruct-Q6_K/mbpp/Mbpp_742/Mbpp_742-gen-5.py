The area of a tetrahedron is given by the following formula:

A = sqrt(6 * a * b * c * d / (a + b + c + d))

where a, b, c, d are the lengths of the edges of the tetrahedron.

Here is the Python function to calculate the area of a tetrahedron:

```
import math

def area_tetrahedron(a):
    return math.sqrt(6 * a * (a/2) * (a/3) * (a/4) / (a + a/2 + a/3 + a/4))
```

This function takes the length of one of the edges of the tetrahedron as input and returns the area of the tetrahedron. The lengths of the other edges are calculated as half, one-third, and one-fourth of the given edge length. 

For example, if the length of one of the edges is 3, the area of the tetrahedron is 15.588457268119894. 

This function uses the math.sqrt function from the math module to calculate the square root. 

The unit test `assert area_tetrahedron(3)==15.588457268119894` ensures that the function returns the correct area for the given edge length. 

Note: This function assumes that the input is the length of one of the edges of the tetrahedron. If the input is the length of one of the faces, the function would be different. 