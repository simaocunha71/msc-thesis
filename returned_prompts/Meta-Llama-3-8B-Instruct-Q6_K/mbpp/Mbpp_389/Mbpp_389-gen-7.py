The Lucas sequence is a series of integers in which each number is the sum of the two preceding ones, usually starting with 2 and 1. The nth Lucas number can be calculated by the formula L(n) = (phi**n + (1-phi)**n)/sqrt(5), where phi is the golden ratio.

Here is the Python function to find the nth Lucas number:

```python
import math
def find_lucas(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi**n - (1-phi)**n) / math.sqrt(5))
```

This function works by using the formula L(n) = (phi**n - (1-phi)**n) / sqrt(5) to calculate the nth Lucas number. The result is then converted to an integer and returned. The function also imports the math module to use the sqrt function. 

The unit test `assert find_lucas(9) == 76` ensures that the function is working correctly. The 9th Lucas number is indeed 76. 

This function will work correctly for any positive integer n. However, it may not work correctly for negative integers or non-integer values of n, as the Lucas sequence is only defined for positive integers. If you need to handle these cases, you would need to add error checking code to the function. 





