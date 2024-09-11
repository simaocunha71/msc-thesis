```
def find_first_occurrence(arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Explanation:
This function uses a binary search algorithm to find the index of the first occurrence of a given number in a sorted array. It starts by initializing the lower and upper bounds of the search range. Then, it enters a while loop that continues until the lower bound is greater than the upper bound. Within the while loop, it compares the target number with the middle element of the current search range. If they are equal, it checks if the middle element is the first occurrence of the target number by comparing the middle element with the previous element in the search range. If the middle element is the first occurrence, it returns the index. Otherwise, it updates the upper bound to be one less than the middle index to continue searching the left half of the search range. If the target number is greater than the middle element, it updates the lower bound to be one greater than the middle index to continue searching the right half of the search range. If the target number is less than the middle element, it updates the upper bound to be one less than the middle index to continue searching the left half of the search range. If the target number is not found after the while loop, it returns -1 to indicate that the target number is not in the array.

The time complexity of this function is O(log n) because it uses a binary search algorithm, which performs at most log n comparisons to find the first occurrence of the target number in a sorted array of length n.

The space complexity of this function is O(1) because it uses a constant amount of additional space to store the lower and upper bounds of the search range, regardless of the size of the input array.

Overall, this function efficiently finds the index of the first occurrence of a given number in a