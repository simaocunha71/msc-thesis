Here is a Python function that reverses an array upto a given position:

```python
def reverse_Array_Upto_K(arr, k):
    left = 0
    right = k - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

In the function `reverse_Array_Upto_K`, `arr` is the array to be reversed and `k` is the given position upto which the array should be reversed. The function uses two pointers, `left` and `right`, starting from the beginning and end of the array respectively. It swaps the elements at the `left` and `right` positions using tuple unpacking, and then moves the `left` pointer one step forward and the `right` pointer one step backward in each iteration until the `left` pointer surpasses the `right` pointer.

To test the function, you can use the provided `assert` statement. The `reverse_Array_Upto_K` function is called with the array `[1, 2, 3, 4, 5, 6]` and the position `4` as arguments. The expected result is `[4, 3, 2, 1, 5, 6]`, which is obtained by reversing the array up to the fourth position.

```python
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
```

This assertion verifies that the `reverse_Array_Upto_K` function correctly reverses the array upto the given position.

```python
def reverse_Array_Upto_K(arr, k):
    left = 0
    right = k - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

To use the function, simply call it with the array and the desired position as arguments. For