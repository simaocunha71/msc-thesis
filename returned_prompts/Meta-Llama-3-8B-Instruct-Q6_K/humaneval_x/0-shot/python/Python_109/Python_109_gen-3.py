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
The function `move_one_ball` checks if the given array can be sorted in non-decreasing order by performing right shift operations. It iterates over the array and checks if any element is greater than its next element. If it finds such an element, it returns `False` as it's not possible to sort the array. If it doesn't find any such element, it returns `True`. If the array is empty, it returns `True` as there's no operation to perform. The function takes O(n) time complexity as it needs to iterate over the array once. The space complexity is O(1) as it doesn't use any extra space.