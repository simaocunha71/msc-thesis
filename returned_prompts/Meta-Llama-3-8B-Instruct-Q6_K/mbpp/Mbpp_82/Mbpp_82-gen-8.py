```
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)
```



The problem asks you to write a function that calculates the volume of a sphere given its radius. The formula for the volume of a sphere is (4/3)πr^3, where r is the radius of the sphere.

The unit test provided ensures that the function works correctly by checking if the result of the function is close to the expected result for a sphere with a radius of 10. This is done using the `math.isclose` function, which checks if two numbers are close to each other within a certain tolerance.

Here is the solution:

```
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)
```

This function takes a single argument `radius`, which is the radius of the sphere. It returns the volume of the sphere calculated using the formula (4/3)πr^3. The `math.pi` constant is used to get the value of pi. The `**` operator is used to raise the radius to the power of 3. The result is then returned by the function.