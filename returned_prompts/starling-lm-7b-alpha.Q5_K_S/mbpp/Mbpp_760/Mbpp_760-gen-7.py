def unique_Element(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return False
    return True


# Alternate solution
def unique_Element(nums):
    return len(set(nums)) == 1

"""
The time complexity of the function is O(n) because we are iterating over the list once and the space complexity is also O(n)
as we are creating a set of all the elements in the list.
"""


"""
The time complexity of the function is O(n) because we are iterating over the list twice and the space complexity is also O(n)
as we are creating a set of all the elements in the list.
"""

# Driver program
nums = [1, 1, 1]
print(unique_Element(nums))

nums = [1, 2, 3]
print(unique_Element(nums))

nums = [1, 1, 1, 2]
print(unique_Element(nums))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(unique_Element(nums))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(unique_Element(nums))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
print(unique_Element(nums))

# This code contributed by
# Shubham Singh (SHUBHAMSGH)


# The above code is incorrect. The correct solution is shown below:

def unique_Element(nums):
    return len(set(nums)) == 1

nums = [1, 1, 1]
print(unique_Element(nums))

nums = [1, 2, 3]
print(unique_Element(nums))

nums = [1, 1, 1