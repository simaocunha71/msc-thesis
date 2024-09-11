```python
def find_first_occurrence(arr, val):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == val:
            if mid == 0 or arr[mid - 1] < val:
                return mid
            else:
                hi = mid - 1
        elif val < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
```

Here is a Python function that performs a binary search to find the first occurrence of a given number in a sorted array. The function takes in two arguments: the sorted array and the number to search for. It returns the index of the first occurrence of the number in the array, or -1 if the number is not present.

The function uses a while loop to iterate until the low and high indices meet or cross each other. Inside the loop, it calculates the middle index using the formula `mid = lo + (hi - lo) // 2`. It then compares the value at the middle index with the target value. If they are equal, it checks if the middle index is the first element of the array or if the value at the previous index is less than the target value. If either condition is true, it returns the middle index as the first occurrence of the target value. Otherwise, it updates the high index to be one less than the middle index to continue searching in the left half of the array. If the target value is less than the value at the middle index, it updates the high index to be one less than the middle index. If the target value is greater than the value at the middle index, it updates the low index to be one more than the middle index.

If the while loop completes without finding the target value, the function returns -1 to indicate that the target value is not present in the array.

The function's time complexity is O(log n) because it performs a binary search. The space complexity is O(1) because it only uses a constant amount of extra space.

To use the function, you can call it with the sorted array and the target value as arguments. In the provided example, `find_first