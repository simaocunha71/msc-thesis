def search(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == nums[mid ^ 1]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

print(search([1,1,2,2,3]))

# In the given array, we use binary search to find the element that appears only once.
# The binary search is modified to find the element that appears only once.
# The mid element is checked to see if it is the same as the next element.
# If it is, then the element is in the first half of the array, and if it's not, then the element is in the second half of the array.
# This is repeated until the left and right pointers meet at the element that appears only once.
# This solution runs in O(log n) time complexity and uses O(1) space.

"""
Explanation:
In the binary search, we compare the mid element with the next element.
If mid is even and the next element is same, then the single element is on the right half.
If mid is odd and the next element is same, then the single element is on the left half.
If mid is even and the next element is not same, then the single element is on the left half.
If mid is odd and the next element is not same, then the single element is on the right half.
"""
<jupyter_output>
3
<jupyter_text>
4. Array - Single Number III
<jupyter_code>
