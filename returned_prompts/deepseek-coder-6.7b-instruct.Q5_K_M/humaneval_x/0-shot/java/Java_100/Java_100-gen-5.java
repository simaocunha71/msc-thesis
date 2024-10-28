Here is the code in Python:

```python
def makeAPile(n):
    levels = []
    if n % 2 == 0:
        for i in range(n):
            levels.append(n + 2 * i)
    else:
        for i in range(n):
            levels.append(n + 2 * i)
    return levels
```

This function takes an integer n as input and returns a list of integers representing the number of stones in each level of the pile. The number of stones in each level is calculated by adding the current level number to the total number of stones in all previous levels.

It starts by checking if n is even. If it is, it adds n + 2 * i (where i is the current level number) to the list of levels for each level from 0 to n. If n is odd, it does the same thing.

Finally, it returns the list of levels.
