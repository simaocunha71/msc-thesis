```
def find_first_occurrence(arr, key):
    # if the array is empty
    if len(arr) == 0:
        return -1
    # if the key is not present in the array
    if key not in arr:
        return -1
    # if the key is present at the first index
    if arr[0] == key:
        return 0
    # if the key is present at the end of the array
    if arr[-1] == key:
        return len(arr) - 1
    # if the key is present between the first and last element
    start = 0
    end = len(arr) - 1
    while start < end:
        # find mid
        mid = (start + end) // 2
        # if the mid element is less than the key
        if arr[mid] < key:
            start = mid + 1
        # if the mid element is greater than the key
        elif arr[mid] > key:
            end = mid - 1
        # if the mid element is equal to the key
        else:
            # if the mid element is equal to the first element
            if arr[mid] == arr[0]:
                return 0
            # if the mid element is equal to the last element
            elif arr[mid] == arr[-1]:
                return len(arr) - 1
            # if the mid element is present between the first and last element
            else:
                return mid
    return -1


# Test
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1
```

Explanation:
The function `find_first_occurrence` takes two arguments: `arr`, which is the sorted array, and `key`, which is the number we want to find the index of its first occurrence.

The function first checks if the array is empty. If it is, it returns -1 because the number cannot be present in an empty array. Then it checks if the key is not present in the array. If it is not, it also returns -