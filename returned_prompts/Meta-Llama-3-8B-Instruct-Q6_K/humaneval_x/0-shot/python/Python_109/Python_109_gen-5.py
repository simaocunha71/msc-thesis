```
def move_one_ball(arr):
    if not arr:
        return True
    
    max_val = max(arr)
    if arr[0] <= max_val:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return True
    return False
```

The function `move_one_ball` checks if it is possible to get an array sorted in non-decreasing order by performing right shift operations. It first checks if the array is empty. If it is, it returns `True`. Then it finds the maximum value in the array. If the first element of the array is less than or equal to the maximum value, it returns `True`. Then it checks if there are any elements in the array that are less than the previous element. If it finds such an element, it returns `True`. If it does not find any such elements, it returns `False`, indicating that it is not possible to get the array in non-decreasing order by performing right shift operations.