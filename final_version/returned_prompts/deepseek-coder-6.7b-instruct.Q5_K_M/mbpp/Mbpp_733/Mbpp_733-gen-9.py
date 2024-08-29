def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid  # found the target, but we need to continue searching to the left to find the first occurrence
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

"""
Explanation:
In the above code, we're using binary search to find the first occurrence of the target in a sorted array. 
First, we initialize two pointers, left and right, to the start and end of the array, respectively. 
We also initialize a variable result to -1, which will be used to store the index of the first occurrence of the target. 

Then, we enter a while loop, which continues until left is less than or equal to right. 
Inside the loop, we calculate the middle index of the current search space. 

If the middle element is equal to the target, we update result to the current middle index, 
and move the right pointer to mid - 1 to continue searching to the left of the array. 

If the middle element is less than the target, we move the left pointer to mid + 1. 

If the middle element is greater than the target, we move the right pointer to mid - 1. 

Finally, we return the result, which will be the index of the first occurrence of the target if it exists in the array, or -1 if it doesn't.
"""

# Time complexity: O(log n)
# Space complexity: O(1)

# 2. Find Peak Element
# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak