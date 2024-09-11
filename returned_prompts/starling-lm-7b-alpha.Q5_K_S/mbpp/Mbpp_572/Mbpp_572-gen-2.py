"""
def two_unique_nums(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

def test_two_unique_nums():
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    print("All tests passed!")

test_two_unique_nums()
"""

def two_unique_nums(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

def test_two_unique_nums():
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    print("All tests passed!")

test_two_unique_nums()






"""
