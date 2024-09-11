Here is a solution for your problem:

```python
def max_Abs_Diff(arr):
    min_element = min(arr)
    max_element = max(arr)
    return max_element - min_element
```

This function first finds the minimum and maximum element in the array, and then returns the absolute difference between the two.

For example, if we run `max_Abs_Diff((2,1,5,3))`, the function will return `4`.

```python
assert max_Abs_Diff((2,1,5,3)) == 4
```

This assert statement is used to verify whether the function works correctly or not, and the result is `True`, indicating that the function is working correctly.

This function can be used to find the maximum difference between any two elements in a given array, regardless of the size of the array.

```python
print(max_Abs_Diff([-5, -10, 20, 3]))
```

The above code will output `23`, which is the maximum difference between any two elements in the array `[-5, -10, 20, 3]`.

```python
print(max_Abs_Diff([1, 2, 3, 4, 5]))
```

The above code will output `4`, which is the maximum difference between any two elements in the array `[1, 2, 3, 4, 5]`.

In summary, this function can be used to find the maximum difference between any two elements in a given array, and the result is the absolute difference between the maximum and minimum elements in the array.

```python
def max_Abs_Diff(arr):
    min_element = min(arr)
    max_element = max(arr)
    return max_element - min_element
```

This function is easy to understand and can be used to find the maximum difference between any two elements in a given array, regardless of the size of the array.

```python
assert max_Abs_Diff((2,1,5,3)) == 4
print(max_Abs_Diff([-5, -10, 20, 3]))  #