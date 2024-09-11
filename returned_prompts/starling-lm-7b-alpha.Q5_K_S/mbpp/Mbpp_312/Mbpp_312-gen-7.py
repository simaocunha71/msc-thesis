"""
import math

def volume_cone(r,h):
    return (1/3) * math.pi * r * r * h

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""

def volume_cone(r,h):
    return (1/3) * math.pi * r * r * h

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)



def volume_cone(r,h):
    return (1/3) * math.pi * r * r * h

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)



# Made By Mostafa_Khaled



```
The provided Python code defines a function called `volume_cone` that calculates the volume of a cone. The function takes two parameters: `r` (the radius of the base of the cone) and `h` (the height of the cone). The formula used to calculate the volume of a cone is `(1/3) * π * r * r * h`. The `math.isclose` function is used to compare the calculated volume with the expected result (314.15926535897927) within a relative tolerance of 0.001. The assertion statement `assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)` checks if the calculated volume is within the desired tolerance.

To use the `volume_cone` function, you can call it with the appropriate values for `r` and `h`, like this:

```python
result = volume_cone(5, 12)
print(result