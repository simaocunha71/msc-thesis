def search(nums):
    for i in range(0, len(nums)-1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]

print(search([1,1,2,2,3]))

"""
Explanation:
The function iterates over the array in steps of 2. If the current element is not equal to the next one, 
it means that the unique number is before this position. If the function has iterated over all elements in this way,
it means that the unique number is the last one, so it returns this number.
"""

# Test cases
assert search([1,1,2,2,3]) == 3
assert search([1,1,2,3,3]) == 2
assert search([1,2,2,3,3]) == 1
assert search([1]) == 1
assert search([1,1,2]) == 2
assert search([1,1,2,2,3,3,4]) == 4
assert search([1,1,2,2,3,3,4,4,5]) == 5
assert search([1,1,2,2,2,3,3,4,4]) == None
assert search([1,1,1,2,2,2,3,3,3,4,4,4,5]) == 5
assert search([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]) == None
assert search([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]) == 6
assert search([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6]) == None
assert search([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]) == None
assert search([1,1,1,2,2,2,3,3,3,4,4,4,5