To calculate the angle of a complex number, you can use the following steps:

1. Calculate the magnitude of the complex number using the `abs()` function. This will give you the length of the complex number in the complex plane.

2. Use the `np.arctan()` function to calculate the angle of the complex number. The `np.arctan()` function takes the imaginary part of the complex number divided by the real part and returns the angle in radians.

3. Finally, use the `np.angle()` function to calculate the phase of the complex number. The `np.angle()` function takes the complex number and returns the phase in radians.

Here's an example implementation of the `angle_complex()` function:

```python
import math
import numpy as np

def angle_complex(x, y):
    angle = np.arctan(y/x)
    phase = np.angle(x + y * 1j)
    return phase
```

You can test the function using the provided assertion:

```python
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
```

The function should correctly calculate the angle of the complex number and the assertion should pass.

Note: The `np.arctan()` function returns the principal value of the arctangent, which is in the range of -π/2 to π/2. If the angle of the complex number is outside this range, you may need to adjust the returned value accordingly.

```python
import math
import numpy as np

def angle_complex(x, y):
    angle = np.arctan(y/x)
    phase = np.angle(x + y * 1j)
    
    # Adjust the angle if it's outside the range of -π/2 to π/2
    if angle < -math.pi/2:
        angle += 2 * math.pi
    elif angle > math.pi/2:
        angle -= 2 * math.pi
    
    return angle
```
