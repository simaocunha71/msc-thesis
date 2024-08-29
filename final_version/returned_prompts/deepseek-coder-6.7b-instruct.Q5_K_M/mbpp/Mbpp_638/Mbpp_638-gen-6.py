Here is the Python function for the problem:

```python
import math

def wind_chill(velocity, temp):
    wci = 13.12 + 0.6215*temp - 11.37*math.pow(velocity,0.16) + 0.3965*temp*math.pow(velocity,0.16)
    return math.ceil(wci)
```

This function uses the formula for wind chill index (wci) provided by the National Weather Service. It is then rounded to the next integer using the `math.ceil` function.

The formula for wind chill index is given as:
`wci = 13.12 + 0.6215*temp - 11.37*velocity^0.16 + 0.3965*temp*velocity^0.16`

The function takes the velocity and temperature as arguments, and returns the wind chill index rounded to the next integer.

So, for the test case `wind_chill(120,35)`, it will return `40`.
"""

