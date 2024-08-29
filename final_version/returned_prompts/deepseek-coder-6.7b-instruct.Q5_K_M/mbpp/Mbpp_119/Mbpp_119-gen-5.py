def search(nums):
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]

print(search([1,1,2,2,3]))

# Time Complexity: O(n)
# Space Complexity: O(1)

# The function is iterating over the list in steps of 2, comparing each pair of elements.
# If it finds a pair where the first element is not equal to the second, it returns the first element,
# which is the element that appears only once in the list. 
# If it doesn't find such a pair, it means that the last element is the one that appears only once,
# so it returns the last element.

# This function works because the input list is sorted. If the input list is not sorted, 
# sorting the list first would make the function work, but it would increase the time complexity.
<jupyter_output>
3
<jupyter_text>
3. Binary SearchGiven a sorted array of integers, find the index of the target value. Return -1 if the target is not in the array.
<jupyter_code>
