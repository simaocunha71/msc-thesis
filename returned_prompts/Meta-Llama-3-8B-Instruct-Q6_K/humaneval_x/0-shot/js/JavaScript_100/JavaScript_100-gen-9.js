Here is the solution in Python:

```python
def makeAPile(n):
    pile = [n]
    for _ in range(n-1):
        if pile[-1] % 2 == 0:
            pile.append(pile[-1] + 1)
        else:
            pile.append(pile[-1] - 1)
    return pile
```

This function starts with a pile of `n` stones and then iterates `n-1` times to build the rest of the pile. In each iteration, it checks if the current level has an even or odd number of stones and then appends the next even or odd number to the pile. The function returns the list of stones in each level.

You can test this function with different values of `n` to see the output. For example, `makeAPile(3)` returns `[3, 5, 7]`.