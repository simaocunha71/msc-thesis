```
def move_one_ball(arr):
    if not arr:
        return True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True
```
This function iterates through the array and checks if any element is greater than the next one. If it finds such an element, it immediately returns `False`, indicating that it is not possible to get the array in non-decreasing order by performing right shift operations.

If the function does not find any such element, it means that the array is already in non-decreasing order or it can be made in non-decreasing order by performing right shift operations, so it returns `True`. If the array is empty, it also returns `True`, as it is trivially possible to get the array in non-decreasing order. 