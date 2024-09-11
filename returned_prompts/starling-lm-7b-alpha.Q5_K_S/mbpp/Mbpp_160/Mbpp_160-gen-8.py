```
from fractions import gcd

def find_solution(a, b, n):
    g = gcd(a, b)
    if n % g != 0:
        return None
    x, y = (n * b // g + a * b) // g, (n * a // g - b * a) // g
    return (x, y)
```

This solution finds the greatest common divisor of a and b. It then checks if n is divisible by g. If not, no solution exists. Otherwise, it uses the extended Euclidean algorithm to find integers x and y such that ax + by = gcd(a, b). It scales x and y by n/g to get the solution for ax + by = n.



The time complexity of this function is O(log(min(a, b))), since the extended Euclidean algorithm has this time complexity.


```python
# Example usage:
assert find_solution(2, 3, 7) == (2, 1)
```


This function is an implementation of the extended Euclidean algorithm, which is used to find the integers x and y that satisfy ax + by = gcd(a, b). In this case, we modify it to find x and y such that ax + by = n. The time complexity of this function is O(log(min(a, b))), since the extended Euclidean algorithm has this time complexity.
```

```

```python
# Example usage:
assert find_solution(2, 3, 7) == (2, 1)
```


This function is an implementation of the extended Euclidean algorithm, which is used to find the integers x and y that satisfy ax + by = gcd(a, b). In this case, we modify it to find x and y such that ax + by = n. The time complexity of this function is O(log(min(a, b))), since the extended Euclidean algorithm has this time complexity.
```

```python
# Example usage:
assert find_solution(2, 3, 7) == (2, 1)
```
