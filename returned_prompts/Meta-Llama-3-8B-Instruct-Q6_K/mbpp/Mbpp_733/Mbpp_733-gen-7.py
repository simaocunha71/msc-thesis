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



The problem asks you to write a function that finds the index of the first occurrence of a given number in a sorted array. 

The function should use binary search to find the index. It starts by considering the middle element of the array. If the middle element is equal to the target, it checks if the target is also present in the left half of the array. If it is, it moves the right pointer to the middle element. If not, it moves the left pointer to the middle element + 1. If the middle element is less than the target, it moves the left pointer to the middle element + 1. If the middle element is greater than the target, it moves the right pointer to the middle element - 1.

The function returns the index of the first occurrence of the target. If the target is not present in the array, it returns -1.

The unit test `assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1` helps to clarify the problem by providing an example of how the function should work. In this case, the function should return 1, which is the index of the first occurrence of 5 in the array. 





The time complexity of this function is O(log n), where n is the length of the array. This is because the function uses binary search, which reduces the search space by half in each iteration. The space complexity is O(1), as the function only uses a constant amount of space to store the indices and the target.