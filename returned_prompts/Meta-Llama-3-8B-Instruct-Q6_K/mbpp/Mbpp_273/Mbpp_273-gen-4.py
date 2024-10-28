You can solve this problem as follows:

```python
def substract_elements(t1, t2):
    return tuple(x - y for x, y in zip(t1, t2))
```


This function takes two tuples `t1` and `t2` as input. It uses the built-in `zip` function to iterate over the elements of both tuples in parallel, subtracting each element of `t1` from the corresponding element of `t2`. The result is a new tuple containing the differences. The `assert` statement in the problem description confirms that this function works as expected. For example, `substract_elements((10, 4, 5), (2, 5, 18))` returns `(8, -1, -13)`.