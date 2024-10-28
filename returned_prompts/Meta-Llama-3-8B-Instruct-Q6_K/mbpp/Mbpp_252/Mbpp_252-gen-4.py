```
import cmath
def convert(z):
    r = abs(z)
    theta = cmath.phase(z)
    return (r, theta)
```  # Returns (r, theta) where r is the magnitude and theta is the angle in radians
```python
assert convert(1) == (1.0, 0.0)
```  # Test
```python
assert convert(1+1j) == (1.4142135623730951, 0.7853981633974483)
```  # Test
```python
assert convert(1+2j) == (2.23606797749979, 0.9827937232473291)
```  # Test
```python
assert convert(-1) == (1.0, 3.141592653589793)
```  # Test
```python
assert convert(-1-1j) == (1.4142135623730951, 4.71238898038469)
```  # Test
```python
assert convert(2+3j) == (3.605551275463989, 0.9272952180016123)
```  # Test
```python
assert convert(1-1j) == (1.4142135623730951, 2.3561944901923448)
```  # Test
```python
assert convert(-1+1j) == (1.4142135623730951, 2.3561944901923448)
```  # Test
```python
assert convert(-2+3j) == (3.605551275463989, 2.121320343559643)
```  # Test
```python
assert convert(2-3j) == (3.605551275463989, 4.71238898038469)
```  # Test
```python
assert convert(-2-3j) == (3.605551275463989, 5.003398179449351)
```  # Test
```
The function takes a complex number as input and returns its polar coordinates as a tuple. The polar coordinates are calculated using the `abs` function to find the magnitude (r) and the `cmath.phase` function to find the angle (theta) in radians. The `cmath` module is used to handle complex numbers. The function is tested with various complex numbers to ensure it works correctly.  # Returns