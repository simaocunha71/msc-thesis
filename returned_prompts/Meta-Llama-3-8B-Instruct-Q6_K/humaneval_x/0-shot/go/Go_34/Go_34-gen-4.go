Here is the Python equivalent of the given problem:

```python
def unique(l):
    return sorted(set(l))
```

Explanation:
The `set` function is used to remove duplicates from the list, and the `sorted` function is used to sort the list in ascending order. This is equivalent to the provided Python code.

For example, if you call `unique([5, 3, 5, 2, 3, 3, 9, 0, 123])`, it will return `[0, 2, 3, 5, 9, 123]`, which is the same output as the provided Python code.