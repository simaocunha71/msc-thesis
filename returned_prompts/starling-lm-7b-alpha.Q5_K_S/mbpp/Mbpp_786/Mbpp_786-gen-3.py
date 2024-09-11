def right_insertion(arr, val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return left

print(right_insertion([1,2,4,5],6))

"""
The above code will return the left index of the right insertion point. To get the index of the right insertion point, we can simply subtract one from the result.

Explanation:

The function uses binary search to find the right insertion point of a value in a sorted array. It starts with a left pointer at the beginning of the array and a right pointer at the end of the array.

The function compares the middle element of the array with the value. If the middle element is less than the value, it updates the left pointer to the middle index + 1. If the middle element is greater than or equal to the value, it updates the right pointer to the middle index - 1.

The function continues this process until the left pointer is greater than the right pointer. At this point, the left pointer points to the right insertion point of the value in the array.

To get the index of the right insertion point, we subtract one from the left pointer.

The time complexity of this algorithm is O(log n), where n is the length of the array.
"""

"""
The above code defines a function called right_insertion that takes in two parameters: arr (the sorted array) and val (the value to insert). It uses binary search to find the right insertion point of the value in the array.

The function initializes left and right pointers to the beginning and end of the array, respectively. It enters a while loop that continues until the left pointer is greater than the right pointer.

Inside the loop, the function calculates the mid index as the average of the left and right pointers. It compares the value at the mid index with the value. If the mid value is less than the value, it updates the left pointer to mid + 1. If the mid value is greater than or equal to the value, it updates