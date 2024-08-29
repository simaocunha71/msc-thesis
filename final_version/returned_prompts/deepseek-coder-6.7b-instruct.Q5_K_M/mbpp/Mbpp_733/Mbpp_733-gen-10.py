def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first_occurrence = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            first_occurrence = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first_occurrence

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))

# Time complexity: O(log n)
# Space complexity: O(1)

"""
Explanation:
This function uses binary search to find the index of the first occurrence of a given number in a sorted array.
We initialize two pointers, low and high, to the start and end of the array respectively.
We then enter a while loop, which continues until low is less than or equal to high.
Inside the loop, we calculate the middle index, mid.
If the middle element is equal to the target, we update first_occurrence to mid and move the high pointer to mid - 1 to continue the search for earlier occurrences.
If the middle element is less than the target, we move the low pointer to mid + 1 to continue the search in the upper half of the array.
If the middle element is greater than the target, we move the high pointer to mid - 1 to continue the search in the lower half of the array.
Finally, we return first_occurrence, which holds the index of the first occurrence of the target in the array.
"""


"""
Other Solution:

def find_first_occurrence(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))
"""

# This solution uses Python'