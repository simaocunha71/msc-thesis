```
def monotonic(l: list):
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    return increasing or decreasing
```


Explanation:
We use the `all` function with a generator expression to check if all elements in the list are monotonically increasing or decreasing. We use the `zip` function to iterate over the list and its subsequent elements. The `all` function returns `True` if all elements in the iterable are true. If the list is monotonically increasing, `x` will be less than or equal to `y` for all `x` and `y` in the list. If the list is monotonically decreasing, `x` will be greater than or equal to `y` for all `x` and `y` in the list. We return `True` if either condition is met, and `False` otherwise.