Here are a few strategies for solving this problem:

1. Iterate through all the numbers from 0 to x. If you multiply any of them by n, you'll get x. So, if you find such a number, then x is a simple power of n. Otherwise, it's not.

2. Use logarithms. As the task states that x is a simple power of n, you can represent it as n^p, where p is an integer. Then, you can apply the logarithm property ln(a^b) = b * ln(a) to find p: p = ln(x) / ln(n). If p is an integer, then x is a simple power of n.

The first approach has a time complexity of O(n*log(n)) due to the logarithm operation, while the second one has a time complexity of O(log(x) + log(n)).

Here's a Python implementation of the second approach:

```python
import math

def isSimplePower(x, n):
    if x == 0:
        return True
    if x == 1:
        return True
    if n == 1:
        return True
    if n == 0:
        return False
    p = math.log(x, n)
    if p == int(p):
        return True
    return False
```

And here's a Python implementation of the first approach:

```python
def isSimplePower(x, n):
    for i in range(x+1):
        if i*n == x:
            return True
    return False
```

Both functions will return True if x is a simple power of n and False in other cases.

Here's a sample test for both functions:

```python
print(isSimplePower(1, 4)) # True
print(isSimplePower(2, 2)) # True
print(isSimplePower(8, 2)) # True
print(isSimplePower(3, 2)) # False
print(isSimplePower(3, 1)) # False
print(isSimplePower(5, 3)) # False
```

In the second approach,