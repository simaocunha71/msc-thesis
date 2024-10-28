```
def move_one_ball(arr):
    if not arr:  # If the array is empty, return True
        return True
    
    max_element = max(arr)  # Find the maximum element in the array
    max_index = arr.index(max_element)  # Find the index of the maximum element
    
    if max_index != 0:  # If the maximum element is not at the beginning
        return False  # Return False
    
    for i in range(1, len(arr)):  # Iterate from the second element to the end
        if arr[i] < arr[i - 1]:  # If an element is smaller than the previous one
            return False  # Return False
    
    return True  # If all conditions are met, return True
```



Here is a Python solution that checks if it is possible to sort the array in non-decreasing order by performing right shift operations.

The function `move_one_ball` first checks if the array is empty. If it is, it returns `True` because it is always possible to sort an empty array.

Then, it finds the maximum element in the array and its index. If the maximum element is not at the beginning of the array, it returns `False` because it is not possible to sort the array in non-decreasing order.

Next, it iterates over the array from the second element to the end. If it finds an element that is smaller than the previous one, it returns `False` because it is not possible to sort the array in non-decreasing order.

If the function has not returned `False` by the end of the iteration, it returns `True` because it is possible to sort the array in non-decreasing order.

The function also handles the case where the array has only one element. In this case, the function returns `True` because it is always possible to sort a single-element array.

The time complexity of this function is O(n), where n is the length of the array, because it iterates over the array once. The space complexity is O(1), because it uses a constant amount of space to store the maximum element and its index.