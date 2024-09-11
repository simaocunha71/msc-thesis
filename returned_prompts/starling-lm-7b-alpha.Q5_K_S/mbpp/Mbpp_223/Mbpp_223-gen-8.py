```
def is_majority(arr, n, element):
    # Get the middle index of the array
    mid = n // 2
    # Check if the element is the middle element of the array
    if element == arr[mid]:
        # Get the left and right neighbor of the middle element
        left_neighbor = arr[mid - 1] if mid > 0 else -1
        right_neighbor = arr[mid + 1] if mid < n - 1 else -1
        # If both neighbors are equal to the middle element, return True
        if left_neighbor == element and right_neighbor == element:
            return True
    # If the element is not the middle element, return False
    return False
```

Here's an example of how to use the function:
```python
arr = [1, 2, 3, 3, 3, 3, 10]
n = len(arr)
element = 3
print(is_majority(arr, n, element))  # Output: True
```

This function checks if the given element is the majority element in the sorted array. It first calculates the middle index of the array and compares the element with the middle element. If they are equal, it checks if the left and right neighbors of the middle element are also equal to the middle element. If all three are equal, the function returns True, indicating that the element is the majority element. Otherwise, it returns False.

In the provided example, the function is used to check if the element 3 is the majority element in the array [1, 2, 3, 3, 3, 3, 10]. Since 3 appears more than half of the length of the array (which is 3.5), the function returns True.

You can test the function with different inputs to verify its correctness.

Explanation:

The function `is_majority` takes in three parameters: `arr`, which is the sorted array, `n`, which is the length of the array, and `element`, which is the element to check.

The function first calculates the middle index of the array by dividing the length by 2. It then compares the element with the middle element of