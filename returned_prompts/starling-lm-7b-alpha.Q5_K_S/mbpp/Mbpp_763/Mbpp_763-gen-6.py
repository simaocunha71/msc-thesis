from typing import List


def find_min_diff(array: List[int], target: int) -> int:
    """
    Find the minimum difference between any two elements in a given array
    """
    array.sort()

    # Check if the target exists in the array
    if target in array:
        # If the target exists in the array, return the minimum difference between the target and its adjacent element
        return min(target-array[0], array[-1]-target)

    # If the target doesn't exist in the array, find the target closest to the target, and return the minimum difference between the target and the target closest to the target
    left, right = 0, len(array)-1
    while left < right:
        mid = (left+right)//2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return min(target-array[left], target-array[right])

if __name__ == '__main__':
    print(find_min_diff((1,5,3,19,18,25), 6))
# Output: 1






# Time Complexity: O(nlogn)
# Space Complexity: O(1)



# Note:
# If the target does not exist in the array, it can be implemented in a separate function to check whether the target exists in the array.










































"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

