def big_diff(lst):
    max_element = max(lst)
    min_element = min(lst)
    return max_element - min_element





























"""
Write a Python function that takes in a list of numbers and returns the difference between the largest and smallest number.

Examples:

big_diff([1,2,3,4]) ➞ 3
big_diff([-2,-1,0,1]) ➞ 3
big_diff([100,10,1]) ➞ 99
"""



```
# Find the difference between the maximum and minimum values
def big_diff(lst):
    return max(lst) - min(lst)
```

A: Here's a Python function that takes in a list of numbers and returns the difference between the largest and smallest number:

```python
def big_diff(lst):
    return max(lst) - min(lst)
```

The function uses the `max()` and `min()` built-in functions in Python to find the maximum and minimum values in the list, respectively. Then, it subtracts the minimum value from the maximum value to find the difference.

For example, if you call `big_diff([1,2,3,4])`, it will return `3` because the maximum value in the list is `4` and the minimum value is `1`. Similarly, if you call `big_diff([-2,-1,0,1])`, it will return `3` because the maximum value is `1` and the minimum value is `-2`. Finally, if you call `big_diff([100,10,1])`, it will return `99` because the maximum value is `100` and the minimum value is `1`.

You can use this function to find the difference between the largest and smallest values in any given list of numbers.
```

```

```

```

```

```

```

```

```

```

```

``