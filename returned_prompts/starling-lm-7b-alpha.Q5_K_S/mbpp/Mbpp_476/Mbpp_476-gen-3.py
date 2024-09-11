def big_sum(arr):
    arr.sort()
    return arr[0]+arr[-1]


# Test
print(big_sum([1,2,3]))  # 4


```

```
"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""

def big_sum(arr):
    arr.sort()
    return arr[0]+arr[-1]
```
In this Python function `big_sum`, the array `arr` is sorted in ascending order by using the `sort()` method. Then, the sum of the smallest value (at index 0) and the largest value (at index -1, which is the last element) is returned. This sum is equal to the sum of the smallest and largest values in the array, as required by the problem statement.

To test the function, the `print()` statement is used to display the result of `big_sum([1,2,3])`, which is `4`.
```

```

```python
"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""

def big_sum(arr):
    arr.sort()
    return arr[0]+arr[-1]

# Test
print(big_sum([1,2,3]))  # 4
```

In this Python function `big_sum`, the array `arr` is sorted in ascending order using the `sort()` method. Then, the sum of the smallest value (at index 0) and the largest value (at index -1, which is the last element) is returned. This sum is equal to the sum of the smallest and largest values in the array, as required by the problem statement.

To test the function, the `print()` statement is used to display the result of `big_sum([1,2,3])`, which is `4`.

```

```

```python
"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum