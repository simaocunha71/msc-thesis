```
def move_one_ball(arr):
    if not arr:
        return True

    arr.sort()
    if arr == sorted(arr):
        return True

    for i in range(len(arr)):
        arr = arr[1:] + [arr[0]]
        if arr == sorted(arr):
            return True

    return False
```
This function checks if it is possible to get a sorted array by performing right shift operations on the given array. 

It first checks if the array is empty. If it is, the function returns True because an empty array is already sorted.

Then it checks if the array is already sorted by comparing it to its sorted version. If it is, the function returns True.

If the array is not sorted, the function performs a right shift operation on the array and checks if the resulting array is sorted. If it is, the function returns True. This process is repeated until all possible right shift operations have been performed.

If none of the right shift operations result in a sorted array, the function returns False. 

The time complexity of this function is O(n log n) due to the sorting operation, and the space complexity is O(n) for storing the sorted array. 





