
def search(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

print(search([1,1,2,2,3]))


"""
Here we use binary search to find the element which appears only once in a sorted array. If the middle element is equal to the element next to it, then the element appears twice and we move the low pointer to mid + 1. Otherwise, the element appears only once and we move the high pointer to mid. At the end of the loop, low will point to the element which appears only once.
"""
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
