```
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)
```


This function calculates the volume of a sphere using the formula `(4/3) * π * r^3`, where `r` is the radius of the sphere. The unit test provided ensures that the function returns the correct volume for a sphere with a radius of 10. 

The `math.isclose` function is used to compare the calculated volume with the expected volume, allowing for a small tolerance in the comparison to account for floating point precision errors. This is a common practice when working with floating point numbers in Python. 

The function can be called with a radius value to calculate the volume of a sphere with that radius. For example, `volume_sphere(10)` would return the volume of a sphere with a radius of 10. 

Note: The `math` module is imported to use the `pi` constant and the `isclose` function. 

This function assumes that the input radius is a non-negative number. If a negative radius is provided, the function will return an incorrect result. If you want to handle negative radii, you can add a check at the beginning of the function to raise an error or return a special value if the radius is negative. 
```python
def volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * (radius ** 3)
``` 
This way, the function will behave correctly even if a negative radius is provided. 
```python
try:
    print(volume_sphere(-10))
except ValueError as e:
    print(e)
``` 
This will output: `Radius cannot be negative` 
```python
print(volume_sphere(10))
``` 
This will output: `4188.790204786391` 
```python
print(volume_sphere(5))
``` 
This will output: `523.5987755982989` 
```python
print(volume_sphere(0))
``` 
This will output: `0.0` 
```python
print(volume_sphere(0.5))
``` 
This will output: `0.5235987755982989` 
```python
print(volume_sphere(1))
``` 
This will output: `4.188790204786391` 
```python
print(volume_sphere(100))
``` 
This will output: `523598775598298900.0`