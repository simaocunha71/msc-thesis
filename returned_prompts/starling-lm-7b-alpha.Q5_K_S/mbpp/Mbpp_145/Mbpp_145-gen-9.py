Here's one way to approach this problem:

```python
def max_Abs_Diff(arr):
    maximum = arr[0]
    minimum = arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    return maximum - minimum
```

Explanation:
This function first initializes two variables, `maximum` and `minimum`, to the first element in the array. It then iterates through the rest of the array, updating `maximum` and `minimum` if a greater or smaller number is found, respectively. Finally, it returns the difference between the maximum and minimum values.

For example, if we call `max_Abs_Diff((2,1,5,3))`, the function will return `4`, which is the maximum difference between any two elements in the array.

The time complexity of this function is O(n), where n is the length of the array, since it only needs to iterate through the array once to find the maximum and minimum values.
```

```

```

```python

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

```

```

```

```python

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

```

```

```

```python

```

```

```

```

```

```python

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

```

```

```

```

```python

```

```

```

```

```

```
