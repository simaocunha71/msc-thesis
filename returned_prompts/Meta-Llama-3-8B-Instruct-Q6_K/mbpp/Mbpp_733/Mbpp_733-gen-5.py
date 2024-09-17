```
def find_first_occurrence(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] < num:
                return mid
            high = mid - 1
    return -1
```


This function uses a binary search algorithm to find the first occurrence of a given number in a sorted array. It starts by finding the middle element of the array. If the middle element is less than the given number, it moves the low pointer to the middle + 1. If the middle element is greater than the given number, it moves the high pointer to the middle - 1. If the middle element is equal to the given number, it checks if the middle element is the first occurrence of the number in the array. If it is, it returns the middle index. If not, it moves the high pointer to the middle - 1. The function continues this process until it finds the first occurrence of the number or the number is not found in the array. If the number is not found, it returns -1. The time complexity of this function is O(log n), where n is the length of the array. The space complexity is O(1), which means the space required does not change with the size of the input array. The function also handles the case where the given number is not present in the array, in which case it returns -1. This function is efficient and scalable for large arrays.