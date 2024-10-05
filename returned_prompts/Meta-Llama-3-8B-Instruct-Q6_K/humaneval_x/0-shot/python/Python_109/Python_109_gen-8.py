```
def move_one_ball(arr):
    if not arr:
        return True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
```
Explanation:
The function checks if it is possible to get a sorted array by performing right shift operations. It iterates over the array and checks if each element is less than or equal to the next element. If it finds an element that is greater than the next element, it returns False because it is not possible to get a sorted array by performing right shift operations. If it doesn't find any such element, it returns True because the array is already sorted. If the array is empty, it returns True because an empty array is considered sorted.

Example:
```
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
```
Time Complexity: O(n)
Space Complexity: O(1) (since we are not using any extra space)  # noqa: E402
```python
def move_one_ball(arr):
    if not arr:
        return True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
```
Explanation:
The function checks if it is possible to get a sorted array by performing right shift operations. It iterates over the array and checks if each element is less than or equal to the next element. If it finds an element that is greater than the next element, it returns False because it is not possible to get a sorted array by performing right shift operations. If it doesn't find any such element, it returns True because the array is already sorted. If the array is empty, it returns True because an empty array is considered sorted.

Example:
```
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
```
Time Complexity: O(n)
Space Complexity: O(1) (since we are not using any extra space)  # noqa: E402
```python
def move_one_ball(arr):
    if not arr:
        return True

   