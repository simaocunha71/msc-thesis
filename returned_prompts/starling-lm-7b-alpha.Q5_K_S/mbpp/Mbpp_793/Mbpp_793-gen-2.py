def last(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == x:
            if mid == len(arr) - 1 or arr[mid + 1] != x:
                return mid
            else:
                start = mid + 1
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# Test
print(last([1,2,3], 1))  # 0
print(last([1,2,3], 2))  # 1
print(last([1,2,3], 3))  # 2
print(last([1,2,3], 4))  # -1
print(last([], 2))  # -1

"""
Time complexity: O(logn)
Space complexity: O(1)
"""

# Reference:
# https://www.geeksforgeeks.org/find-last-occurrence-element-sorted-array/

"""
This function follows a binary search algorithm to find the last occurrence of an element in a sorted array.
It maintains two pointers, start and end, initially pointing to the first and last indices of the array.
While the start pointer is less than or equal to the end pointer, it calculates the mid index as the average of the start and end pointers.
If the element at the mid index is equal to the target element, it checks if the mid index is the last index of the array or if the element at the next index is not equal to the target element.
If either condition is true, it returns the mid index as the last occurrence of the target element.
Otherwise, it updates the start pointer to mid + 1 to search in the right half of the array.
If the target element is greater than the element at the mid index, it updates the start pointer to mid + 1 to search in the right half of the array.
If the target element is less than the element at the mid index, it updates the end pointer to mid - 1 to search in the left half of the