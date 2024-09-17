The nth Catalan number is the nth number in the sequence of Catalan numbers, which is a sequence of natural numbers that occur in various counting problems about nested parentheses, binary trees, and other recursive structures.

The formula for the nth Catalan number is: C(n) = (2n)! / ((n+1)! * n!)

Here is a Python function that calculates the nth Catalan number:

```python
import math

def catalan_number(n):
    return math.comb(2*n, n) // (n+1)
```

This function uses the math.comb function from Python 3.8 onwards to calculate the binomial coefficient (2n choose n), and then divides it by (n+1) to get the nth Catalan number.

For example, catalan_number(10) returns 16796, which is the correct value for the 10th Catalan number.

Note that the math.comb function is not available in Python 3.7 or earlier, so if you need to support those versions, you will need to use a different method to calculate the binomial coefficient. One way to do this is to use the formula for the binomial coefficient:

```python
import math

def catalan_number(n):
    result = 1
    for i in range(1, n+1):
        result = result * (2*n - i + 1) // i
    return result // (n+1)
```

This function uses a loop to calculate the binomial coefficient, and then divides the result by (n+1) to get the nth Catalan number. This function should work in Python 3.7 or earlier. However, it is less efficient than the version that uses math.comb, and it may be slower for large values of n.