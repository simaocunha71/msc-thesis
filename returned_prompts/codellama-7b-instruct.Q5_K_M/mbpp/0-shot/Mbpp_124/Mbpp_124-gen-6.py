```
from cmath import polar

def angle_complex(real, imag):
    return polar(real + imag * 1j)[1] * 180 / math.pi
```
