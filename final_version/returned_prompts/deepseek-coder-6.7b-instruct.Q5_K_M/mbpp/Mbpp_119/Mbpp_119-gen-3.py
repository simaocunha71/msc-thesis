def search(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

print(search([1,1,2,2,3])) # 3

# This solution uses binary search to find the element that appears only once in a sorted array.
# If the middle element is equal to its next (or previous in case of an odd index) element, then the element appears an even number of times and we look to the right of the middle.
# Otherwise, we look to the left of the middle. The loop continues until we find the element that appears only once.

# The "mid ^ 1" is used to get the index of the next element. If mid is even, it gives the index of the next element, and if mid is odd, it gives the index of the previous element.
# This is a bitwise XOR operation that flips the least significant bit, which is used to switch between the next and previous element.
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
