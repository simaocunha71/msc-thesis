```
def unique(l: list):
    return sorted(set(l))
```


Explanation:

*   The `set` function is used to remove duplicate elements from the list.
*   The `sorted` function is used to sort the resulting set in ascending order.
*   The `unique` function returns the sorted set as a list.

Here's the result of running the test case provided:

```
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

As you can see, the function correctly returns the sorted unique elements in the list.