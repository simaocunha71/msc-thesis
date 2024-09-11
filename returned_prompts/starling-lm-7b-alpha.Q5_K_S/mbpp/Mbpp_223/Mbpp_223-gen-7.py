```
def is_majority(arr, n, elem):
    if arr[n // 2] == elem:
        return True
    else:
        return False
```

Here's an example of how you can use the function:

```python
arr = [1, 2, 3, 3, 3, 3, 10]
n = 7
elem = 3

result = is_majority(arr, n, elem)
print(result)  # Output: True
```

In this example, the function `is_majority` is called with the sorted array `arr`, its length `n`, and the element `elem`. The function returns `True` if `elem` is the majority element in the array, and `False` otherwise.

To determine if `elem` is the majority element, the function compares the element at the middle index of the array (`arr[n // 2]`) with `elem`. If they are equal, it means that `elem` is the majority element and the function returns `True`. Otherwise, it returns `False`.

You can use this function to check if a given element is the majority element in a sorted array efficiently.

Note: The function assumes that the input array is already sorted in ascending order. If the array is not sorted, you may need to sort it before using this function.

Additionally, it's worth mentioning that the definition of a "majority element" in this context is a bit unusual since it requires the element to occur more than `n/2` times in the array. In most cases, a majority element is defined as an element that occurs more than half of the total number of elements in the array (i.e., `n` divided by 2, rounded up).

However, the provided function adheres to the specific requirement mentioned in the problem statement.

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```