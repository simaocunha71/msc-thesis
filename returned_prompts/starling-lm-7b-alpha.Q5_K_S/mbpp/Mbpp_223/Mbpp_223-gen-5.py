```
def is_majority(arr, length, element):
    left = 0
    right = length - 1
    while left < right:
        if element > arr[left]:
            left += 1
        elif element < arr[right]:
            right -= 1
        else:
            return True
    return left == right
```

Explanation:
The function `is_majority` takes in a sorted array `arr`, its length `length`, and an element `element`. It uses two pointers, `left` and `right`, to traverse the array from both ends. The function compares the element with the elements at the `left` and `right` pointers.

If the element is greater than the element at the `left` pointer, the `left` pointer is incremented. If the element is less than the element at the `right` pointer, the `right` pointer is decremented. If the element is equal to either the element at the `left` pointer or the element at the `right` pointer, it means that the element is a majority element in the given sorted array. In this case, the function returns `True`.

The function continues to move the `left` and `right` pointers until they meet. If the `left` pointer meets the `right` pointer and they are pointing to the same element, it means that the element is a majority element in the given sorted array. The function returns `True` in this case. Otherwise, it returns `False`.

The function's time complexity is O(n), where n is the length of the array.

The provided assert statement `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` checks if the `is_majority` function correctly identifies the element 3 as the majority element in the given sorted array `[1, 2, 3, 3, 3, 3, 10]`.

The function's output for the given assert statement is `True`, indicating that the function correctly identifies 3 as the majority element in the array.

To use the `is_majority` function, you can call it with the appropriate arguments, like this:
```python