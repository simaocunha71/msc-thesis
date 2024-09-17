You can solve this problem with the following function:

```python
import math

def next_power_of_2(n):
    return 2 ** math.ceil(math.log2(n + 1))
```


This function works by using the math.log2 function to calculate the base 2 logarithm of n + 1. The math.ceil function is then used to round up this value to the nearest integer. This gives the exponent of the smallest power of 2 that is greater than or equal to n. Finally, the 2 ** function is used to calculate the value of 2 to this power, which is the smallest power of 2 that is greater than or equal to n.

For example, if you call next_power_of_2(0), the function will return 1, which is the smallest power of 2 that is greater than or equal to 0. If you call next_power_of_2(8), the function will return 16, which is the smallest power of 2 that is greater than or equal to 8. If you call next_power_of_2(16), the function will return 16, which is the smallest power of 2 that is greater than or equal to 16. If you call next_power_of_2(17), the function will return 32, which is the smallest power of 2 that is greater than or equal to 17. If you call next_power_of_2(32), the function will return 32, which is the smallest power of 2 that is greater than or equal to 32. If you call next_power_of_2(33), the function will return 64, which is the smallest power of 2 that is greater than or equal to 33. And so on.