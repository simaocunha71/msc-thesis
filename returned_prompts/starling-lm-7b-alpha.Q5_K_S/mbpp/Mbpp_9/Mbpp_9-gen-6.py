Here is one way to do it:

```python
def find_Rotations(s):
    n = len(s)
    for i in range(1, n):
        if s[:i] + s[i:] == s:
            return i
    return n
```

In this code, we iterate over the length of the string, taking a slice of the string from the start to the end. If we concatenate this slice to the front of the string, the resulting string should be the same as the original. We return the length of the slice if the condition is satisfied, and if not, we return the length of the string itself.

This is a very simple and straightforward solution, but there may be more efficient solutions out there.

Another approach is to use the fact that the result of the rotation is unique. If we rotate the string by k positions, the result will be the same if and only if gcd(n, k) == 1, where n is the length of the string. Therefore, we can use this property to find the minimum number of rotations required to get the same string.

Here is an example implementation of this approach:

```python
def find_Rotations(s):
    n = len(s)
    for k in range(1, n):
        if gcd(n, k) == 1:
            return k
    return None
```

In this code, we iterate over the range of 1 to the length of the string, checking if the gcd of the length of the string and the current iteration is equal to 1. If it is, we return the current iteration. If none of the iterations satisfy the condition, we return None, indicating that no valid rotation was found.

This approach is more efficient than the previous one, especially for large strings, because it only requires a single iteration over the range of rotations. However, it may be less intuitive and less straightforward than the previous solution.

Both of these solutions should work correctly for the given problem, but you can choose the one that suits your needs and preferences best.
```

```
1
```

The first solution is a simple and straightforward approach that involves checking each possible rotation of the string to find the minimum number of rotations required to