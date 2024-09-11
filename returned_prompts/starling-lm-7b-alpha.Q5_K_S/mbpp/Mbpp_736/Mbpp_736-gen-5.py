def left_insertion(nums, target):
    index = 0
    while index < len(nums) and nums[index] < target:
        index += 1
    return index


"""
The above function is correct, but the time complexity is too high, O(n).
Here is a more efficient solution:
"""
def left_insertion(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# Test
print(left_insertion([1,2,4,5],6) == 4)
print(left_insertion([1,2,4,5],3) == 2)
print(left_insertion([1,2,4,5],1) == 0)
print(left_insertion([1,2,4,5],5) == 4)
print(left_insertion([1,2,4,5],0) == 0)
print(left_insertion([],1) == 0)
print(left_insertion([100],100) == 0)
print(left_insertion([100],200) == 1)
print(left_insertion([100],-200) == 0)
print(left_insertion([100,200],-200) == 0)
print(left_insertion([100,200],0) == 1)
print(left_insertion([100,200],100) == 2)
print(left_insertion([100,200],200) == 3)
print(left_insertion([100,200,300],300) == 3)
print(left_insertion([100,200,300],320) == 4)
print(left_insertion