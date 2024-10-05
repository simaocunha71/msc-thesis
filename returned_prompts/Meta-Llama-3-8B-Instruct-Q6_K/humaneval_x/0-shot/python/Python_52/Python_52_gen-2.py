```
def below_threshold(l: list, t: int):
    return all(i < t for i in l)
```
Explanation:
The `all` function returns `True` if all elements of the iterable (in this case, the generator expression `i < t for i in l`) are `True`. The generator expression iterates over each element `i` in the list `l` and checks if it is less than the threshold `t`. If any element is not less than `t`, the `all` function will return `False`. Otherwise, it returns `True`. This is a concise and efficient way to check if all numbers in the list are below the threshold.