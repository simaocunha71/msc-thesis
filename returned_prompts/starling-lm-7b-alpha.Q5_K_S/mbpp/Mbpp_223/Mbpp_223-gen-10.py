```
def is_majority(arr, n, elem):
    mid = n//2
    left = 0
    right = n-1
    while left < right:
        if arr[left] == elem:
            left += 1
        if arr[right] == elem:
            right -= 1
        if arr[left] != elem:
            right = left - 1
        if arr[right] != elem:
            left = right + 1
    return left > mid
```

In this implementation, the function `is_majority` takes in a sorted array `arr`, its length `n`, and an element `elem`. It uses two pointers, `left` and `right`, to traverse the array from both ends. The function compares `elem` with the elements at `left` and `right` pointers. If `elem` is equal to the element at the `left` pointer, it increments the `left` pointer. If `elem` is equal to the element at the `right` pointer, it decrements the `right` pointer. If `elem` is not equal to the element at the `left` pointer, it sets the `right` pointer to the position of the `left` pointer minus one. Similarly, if `elem` is not equal to the element at the `right` pointer, it sets the `left` pointer to the position of the `right` pointer plus one. This process continues until the `left` pointer is greater than the `mid` position of the array, which indicates that `elem` is a majority element in the array. The function returns `True` if `elem` is a majority element, and `False` otherwise.

To test the function, the provided assertion `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` is used. This assertion checks if the function correctly identifies `3` as the majority element in the given array.

You can use this function to determine if an element is a majority element in a sorted array.

Here are some additional examples of how you can use this function:

```python
# Example 1
arr = [1, 1, 2, 2, 3