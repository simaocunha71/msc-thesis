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
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
