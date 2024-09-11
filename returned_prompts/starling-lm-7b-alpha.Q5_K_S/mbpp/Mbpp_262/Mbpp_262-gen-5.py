def split_two_parts(nums, L):
    l1 = nums[:L]
    l2 = nums[L:]
    return (l1, l2)


# print(split_two_parts([1,1,2,3,4,4,5,1],3))
# print(split_two_parts([1,1,2,3,4,4,5,1],2))
# print(split_two_parts([1,1,2,3,4,4,5,1],0))
# print(split_two_parts([1,1,2,3,4,4,5,1],5))
# print(split_two_parts([1,1,2,3,4,4,5,1],6))
# print(split_two_parts([1,1,2,3,4,4,5,1],7))



def split_two_parts(nums, L):
    return (nums[:L], nums[L:])

# print(split_two_parts([1,1,2,3,4,4,5,1],3))
# print(split_two_parts([1,1,2,3,4,4,5,1],2))
# print(split_two_parts([1,1,2,3,4,4,5,1],0))
# print(split_two_parts([1,1,2,3,4,4,5,1],5))
# print(split_two_parts([1,1,2,3,4,4,5,1],6))
# print(split_two_parts([1,1,2,3,4,4,5,1],7))


"""
def split_two_parts(nums, L):
    l1 = nums[:L]
    l2 = nums[L:]
    return (l1, l2)
"""
"""
def split_two_parts(nums, L):
    return (nums[:L], nums[L:])
"""


"""
def split_two_parts(nums, L):