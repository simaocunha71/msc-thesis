```
def find_first_occurrence(arr, key):
    # Start and end index of the array
    start = 0
    end = len(arr) - 1

    # If the key is not present in the array
    if (key < arr[start] or key > arr[end]):
        return -1

    # Find the middle index
    mid = (start + end) // 2

    # If the key is present at the middle itself
    if (arr[mid] == key):
        return mid

    # If the key is smaller than the middle element
    if (key < arr[mid]):
        # It can only be present in the left subarray
        return find_first_occurrence(arr[:mid], key)

    # Else the key can only be present in the right subarray
    return find_first_occurrence(arr[mid+1:], key)
```

This function uses a binary search approach to find the first occurrence of a given number in a sorted array. The function takes in two parameters: the sorted array `arr` and the number `key` to be searched. It initializes the start and end index of the array and checks if the key is outside the range of the array. If so, it returns -1 indicating that the key is not present in the array.

The function then finds the middle index of the array by dividing the sum of the start and end indices by 2. If the middle element of the array is equal to the key, the function returns the middle index as the first occurrence of the key.

If the key is smaller than the middle element, the function recursively calls itself with the left subarray of the middle index. This is because the key can only be present in the left subarray if it is smaller than the middle element.

If the key is larger than the middle element, the function recursively calls itself with the right subarray of the middle index. This is because the key can only be present in the right subarray if it is larger than the middle element.

By using this binary search approach, the function efficiently finds the index of the first occurrence of a given number in a sorted array.

The time complexity of this function is O(log n), where n