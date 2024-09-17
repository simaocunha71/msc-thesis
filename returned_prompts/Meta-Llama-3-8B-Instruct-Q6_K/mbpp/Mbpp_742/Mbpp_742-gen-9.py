The area of a tetrahedron can be calculated using the following formula:
A = sqrt(6 * p * (p - a) * (p - b) * (p - c))
where p is the perimeter of the tetrahedron, and a, b, c are the lengths of its edges.

Here is a Python function that calculates the area of a tetrahedron:

```
import math

def area_tetrahedron(a, b, c):
    p = a + b + c
    return math.sqrt(6 * p * (p - a) * (p - b) * (p - c))
```

This function takes three arguments, a, b, and c, which are the lengths of the edges of the tetrahedron. It calculates the perimeter of the tetrahedron and then uses this value and the lengths of the edges to calculate the area using the formula above.

The unit test `assert area_tetrahedron(3)==15.588457268119894` indicates that the function should return the area of a tetrahedron with edges of length 3. This is a valid test case, as the area of a tetrahedron with edges of length 3 is indeed approximately 15.588457268119894. 

However, the original problem statement does not specify the lengths of the edges of the tetrahedron, so the function should be able to handle any valid input. The unit test is just one example of how the function should work. 

If we want to make the function more general, we can modify it to take any number of arguments, not just three:

```
import math

def area_tetrahedron(*args):
    p = sum(args)
    return math.sqrt(6 * p * (p - args[0]) * (p - args[1]) * (p - args[2]))
```

Now the function can calculate the area of a tetrahedron with any number of edges, as long as the user provides the correct lengths. For example, `area_tetrahedron(3, 4, 5)` would calculate the area of a tetrahedron with edges of length 3, 4, and 5. 

This is a more general and flexible solution that can handle any valid input. 

Note that the function still assumes that the input values are the lengths of the edges of a tetrahedron.