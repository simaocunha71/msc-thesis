"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""

def filter_oddnumbers(nums):
    result = []
    odd = False
    for i in nums:
        if(i % 2 == 0):
            even = True
            break
        else:
            even = False
        if(even):
            pass
        elif(not odd and not even) or (odd and odd==True):
            result.append(nums[i])
    return result