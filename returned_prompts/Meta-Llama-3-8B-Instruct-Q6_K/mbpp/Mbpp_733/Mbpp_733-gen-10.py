```
def find_first_occurrence(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            if mid == 0 or arr[mid - 1] < num:
                return mid
            right = mid - 1
    return -1
```


This function uses a binary search algorithm to find the first occurrence of a given number in a sorted array. It starts by considering the middle element of the array. If the middle element is less than the target number, it moves the left pointer to the right of the middle element. If the middle element is greater than the target number, it moves the right pointer to the left of the middle element. If the middle element is equal to the target number, it checks if the previous element is less than the target number. If it is, it returns the index of the middle element as the first occurrence of the target number. If it is not, it moves the right pointer to the left of the middle element. If the target number is not found, it returns -1. The time complexity of this function is O(log n), where n is the length of the array. The space complexity is O(1). The unit test `assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1` ensures that the function returns the correct index of the first occurrence of a given number in a sorted array.