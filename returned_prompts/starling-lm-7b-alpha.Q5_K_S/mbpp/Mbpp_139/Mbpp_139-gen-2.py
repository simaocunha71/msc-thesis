"""
Here's a function that calculates the circumference of a circle using the formula C = 2 * pi * r:

```python
import math

def circle_circumference(radius):
    return 2 * math.pi * radius
```

To test the function, you can use the `math.isclose()` function to check if the calculated circumference is close to the expected result (62.83). The `rel_tol` parameter specifies the relative tolerance between the two values, and in this case, it's set to 0.001 (or 0.1%).

Here's an example of how you can use the function and assert the result:

```python
import math

def circle_circumference(radius):
    return 2 * math.pi * radius

# Testing the function
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
```

By running this code, you'll get the expected result, passing the assertion.
"""

# Here's a Python function that calculates the circumference of a circle:

import math

def circle_circumference(radius):
    return 2 * math.pi * radius

# Here's an example of how you can use the function and assert the result:

# Testing the function
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)

# This code will pass the assertion and print "OK" if the calculated circumference is within the specified tolerance of the expected result.

"""
Here's a Python function that calculates the circumference of a circle:

```python
import math

def circle_circumference(radius):
    return 2 * math.pi * radius
```

To test the function, you can use the `math.isclose()` function to check if the calculated circumference is close to the expected result (62.83). The `rel_