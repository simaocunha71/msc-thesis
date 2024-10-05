
Here is the Python solution:

```Python
def BelowThreshold(l, t):
    for v in l:
        if v >= t:
            return False
    return True
```
Explanation:

1. We loop through each element `v` in the list `l` using a for loop.
2. For each element, we check if it's greater than or equal to the threshold `t`. If it is, we immediately return `False`, indicating that not all numbers in the list are below the threshold.
3. If we reach the end of the loop without returning `False`, it means that all elements in the list are below the threshold, so we return `True`.

You can test this function with the examples you provided:
```Python
print(BelowThreshold([1, 2, 4, 10], 100)) # True
print(BelowThreshold([1, 20, 4, 10], 5)) # False
```
This should output:
```
True
False
```