```
def last(arr, element):
    for i in reversed(range(len(arr))):
        if arr[i] == element:
            return i
    return -1
```
This function iterates over the array in reverse order and returns the index of the last occurrence of the given element. If the element is not found, it returns -1. The unit test `assert last([1,2,3],1) == 0` ensures that the function returns the correct index for the last occurrence of the element. 

Note: This function has a time complexity of O(n), where n is the length of the array, because it iterates over the entire array in the worst case. If the array is very large, this function may be slow. In that case, a more efficient solution using a binary search algorithm could be used. 

Here is a binary search solution:
```
def last(arr, element):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            if mid == len(arr) - 1 or arr[mid + 1] != element:
                return mid
            right = mid - 1
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
This function uses a binary search algorithm to find the last occurrence of the given element in the array. It returns the index of the last occurrence of the element. If the element is not found, it returns -1. The time complexity of this function is O(log n), making it more efficient for large arrays. 