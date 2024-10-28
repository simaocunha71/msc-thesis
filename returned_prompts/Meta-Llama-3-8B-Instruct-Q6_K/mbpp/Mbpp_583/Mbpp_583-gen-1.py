The nth Catalan number can be calculated using the formula: C(n) = (2n)! / ((n+1)! * n!), where n is a positive integer.

Here is the Python code to calculate the nth Catalan number:

```python
import math

def catalan_number(n):
    return math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))
```

This function uses the math.factorial function to calculate the factorial of a number. The // operator is used for integer division, which is used to avoid floating point division.

The unit test `assert catalan_number(10)==16796` is used to verify that the function is working correctly. The 10th Catalan number is indeed 16796. 

This function will work correctly for any positive integer n. For example, `catalan_number(5)` will return 42, which is the 5th Catalan number. 

Please note that the Catalan numbers are named after the mathematician Eugène Charles Catalan, who first studied them in the 19th century. They have many applications in combinatorics, computer science, and other fields. 