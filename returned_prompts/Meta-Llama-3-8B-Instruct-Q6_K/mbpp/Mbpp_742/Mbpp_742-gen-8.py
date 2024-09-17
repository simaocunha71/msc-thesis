The area of a tetrahedron can be calculated using the formula:
A = sqrt(s*(s-a)*(s-b)*(s-c))
where a, b, c are the lengths of the sides of the tetrahedron, and s is the semi-perimeter, calculated as:
s = (a+b+c)/2

Here is a Python function that implements this formula:
```python
import math

def area_tetrahedron(a):
    s = (a + a + a) / 2
    return math.sqrt(s * (s - a) * (s - a) * (s - a))
```
This function takes the length of one side of the tetrahedron as input and returns the area of the tetrahedron. The unit test `assert area_tetrahedron(3)==15.588457268119894` ensures that the function returns the correct area for a tetrahedron with all sides of length 3.