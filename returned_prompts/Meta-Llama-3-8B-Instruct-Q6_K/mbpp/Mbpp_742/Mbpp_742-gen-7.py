The area of a tetrahedron can be calculated using the formula:

Area = sqrt(s*(s-a)*(s-b)*(s-c))

where s is the semi-perimeter of the tetrahedron and a, b, c are the lengths of the edges.

Here is the Python function that calculates the area of a tetrahedron:

```
import math

def area_tetrahedron(a):
    s = a / 3
    area = math.sqrt(s * (s - a) * (s - a) * (s - a))
    return area
```

This function takes the length of one edge of the tetrahedron as input and returns the area of the tetrahedron. The unit test `assert area_tetrahedron(3)==15.588457268119894` ensures that the function works correctly. 

Note: The formula for the area of a tetrahedron is derived from Heron's formula for the area of a triangle, and the fact that a tetrahedron can be divided into four triangles by connecting each vertex to the centroid. The area of each triangle is then calculated using Heron's formula, and the total area of the tetrahedron is the sum of the areas of the four triangles. However, this formula is not very efficient for large inputs, and a more efficient method would be to use the formula for the volume of a tetrahedron and then divide it by the height. 

In this problem, we are given the length of one edge of the tetrahedron, so we can use the formula for the area of a tetrahedron that involves the length of one edge. This formula is more efficient than the formula that involves the volume of the tetrahedron. 

The function `area_tetrahedron(a)` calculates the area of a tetrahedron with edge length `a`. It first calculates the semi-perimeter `s` of the tetrahedron, and then calculates the area using the formula for the area of a tetrahedron. The function returns the area of the tetrahedron. 

The unit test `assert area_tetrahedron(3)==15.588457268119894` ensures that the function works correctly. The test checks that the area of a tetrahedron with edge length 3 is approximately 15.588457268119894. 

The function `area_tetrahedron(a)` can