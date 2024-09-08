def search(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] != nums[mid + 1]:
            right = mid
        else:
            left = mid + 2
    return nums[left]

print(search([1,1,2,2,3]))  # 3


"""
Explanation:
This problem is a variation of the binary search algorithm. 
The binary search algorithm works by dividing the sorted array into two halves and determining which half contains the unique element. 
However, in this case, we also need to consider the element next to the mid element.

The binary search starts with two pointers, left and right, that initially point to the start and end of the array. 
The middle element is found by taking the average of left and right, and if it is an odd number, subtract 1 to make it even. 

If the middle element is equal to the next element, then the unique element must be on the right half of the array. 
Therefore, we update left to be mid + 2. 

Otherwise, the unique element must be on the left half of the array. So, we update right to be mid. 

We continue this process until left equals right, and return nums[left] as the unique element.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
