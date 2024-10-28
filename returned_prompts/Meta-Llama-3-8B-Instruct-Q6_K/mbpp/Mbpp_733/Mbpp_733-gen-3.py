```
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            right = mid - 1
    return -1
```


The problem is asking to find the index of the first occurrence of a given number in a sorted array. 

The given unit test `assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1` suggests that the array is sorted and we need to find the index of the first occurrence of the target number.

To solve this problem, we can use a binary search algorithm. We start by finding the middle element of the array. If the middle element is equal to the target number, we check if it's the first occurrence by looking at the previous element. If the previous element is less than the target, then the current element is the first occurrence. If the previous element is equal to the target, then we need to search to the left of the middle element. If the middle element is less than the target, then we search to the right of the middle element. If the middle element is greater than the target, then we search to the left of the middle element.

Here is the Python solution:
```
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            right = mid - 1
    return -1
```
This function returns the index of the first occurrence of the target number in the array. If the target number is not found, it returns -1. The time complexity of this function is O(log n), where n is the length of the array. The space complexity