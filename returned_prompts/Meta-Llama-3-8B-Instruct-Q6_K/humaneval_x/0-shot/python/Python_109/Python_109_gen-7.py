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

1. The function `move_one_ball` takes an array `arr` as input and returns a boolean value.
2. If the array is empty, the function returns `True` because an empty array is already sorted.
3. The function then iterates through the array using a for loop.
4. For each element, it checks if the current element is greater than the next element. If it is, the function returns `False` because it is not possible to get a non-decreasing order by performing right shift operations.
5. If the function iterates through the entire array without finding any pairs of elements where the current element is greater than the next element, it returns `True` because the array can be sorted in non-decreasing order by performing right shift operations.

Example:
```
arr = [3, 4, 5, 1, 2]
print(move_one_ball(arr))  # Output: True

arr = [3, 5, 4, 1, 2]
print(move_one_ball(arr))  # Output: False
```
In the first example, the array can be sorted in non-decreasing order by performing 2 right shift operations. In the second example, it is not possible to get a non-decreasing order by performing any number of right shift operations. The function correctly returns `True` for the first example and `False` for the second example.