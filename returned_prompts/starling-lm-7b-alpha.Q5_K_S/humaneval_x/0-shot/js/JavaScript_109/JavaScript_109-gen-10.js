To solve this problem we can follow the steps below:

1. First, we need to find the maximum element in the array. We can do this by iterating through the array and keeping track of the maximum value we have seen so far.
2. Once we have found the maximum element, we can use it as a reference point to compare the other elements in the array. We can start from the second-to-last element and move backwards towards the first element. If an element is greater than the maximum, we know that it is out of order and cannot be sorted using a right shift operation. In this case, we can return false.
3. If all elements are less than or equal to the maximum, we can return true, indicating that it is possible to sort the array using a right shift operation.

Here is the code that implements these steps:

```python
def moveOneBall(arr):
    max_element = max(arr)
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > max_element:
            return False
    return True
```
This code first finds the maximum element in the array using the `max()` function. Then, it iterates through the array in reverse order using a `for` loop, starting from the second-to-last element and moving backwards towards the first element. Inside the loop, it checks if the current element is greater than the maximum element. If it is, the function returns `False`, indicating that it is not possible to sort the array using a right shift operation. If all elements are less than or equal to the maximum, the function returns `True`, indicating that it is possible to sort the array using a right shift operation.

For example, if we call `moveOneBall([3, 4, 5, 1, 2])`, the maximum element in the array is `5`. The function will then compare `5` with the other elements in the array in reverse order: `4`, `3`, `2`, `1`. Since all elements are less than or equal to `5`, the function will return `True`.

On the other hand, if we call `moveOneBall([3, 5, 4, 1, 2])`, the maximum element in the array is `5`. The function will compare `5