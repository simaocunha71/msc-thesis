        long result = 1;
        for(int i = n; i > 0; i--) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        long result = 1;
        for(int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}


A: Here is a Python solution for the problem.

```python
import math

def specialFactorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n  * (n-1)  * (n-2)  * ... * 1
    where n > 0
    """
    result = 1
    for i in range(1, n+1):
        result *= math.factorial(i)
    return result
```

This Python function uses the built-in factorial function from the math module to compute the factorial of each integer from 1 to n, and then multiplies these together to get the special factorial of n.

The math.factorial function raises a ValueError if its argument is a negative integer, or a TypeError if its argument is not an integer. However, the problem statement guarantees that n will be a positive integer, so these errors should not occur.

You can call the function with a positive integer as argument to get the special factorial of that integer. For example:

```python
print(specialFactorial(4))  # Outputs: 288
```

This will compute the special factorial of 4 (which is 4 * 3 * 2 * 1 = 288) and print the result.
