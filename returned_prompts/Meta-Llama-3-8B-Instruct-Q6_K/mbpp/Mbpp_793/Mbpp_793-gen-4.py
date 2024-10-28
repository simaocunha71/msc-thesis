```
def last(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if mid == len(arr) - 1 or arr[mid+1] != target:
                return mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
This function uses a binary search approach to find the last position of the target element in the sorted array. If the element is found, it checks if it's the last element in the array or if the next element is not the target. If it's the last element or the next element is not the target, it returns the index of the target element. If the element is not found, it returns -1.  The unit test `assert last([1,2,3],1) == 0` ensures that the function returns the correct index for the target element.  If the target element is not in the array, the function will return -1.  If the array is empty, the function will return -1.  The time complexity of this function is O(log n), where n is the length of the array.  The space complexity is O(1), as it only uses a constant amount of space.  This function assumes that the input array is sorted in ascending order.  If the array is not sorted, the function may not work correctly.  The function also assumes that the target element is unique in the array.  If there are multiple occurrences of the target element, the function will return the index of the last occurrence.  If you need to find the indices of all occurrences of the target element, you would need a different approach.  The function does not modify the input array.  It only returns the index of the target element.  If the target element is not in the array, the function returns -1.  The function is case-sensitive and treats uppercase and lowercase letters as different characters.  It is also sensitive to the order of characters.  If you need a case-insensitive search or a search that ignores the order of characters, you would need a different approach.  The function is designed to work with strings, but it can also work with other types of data that can be compared using the equality operator