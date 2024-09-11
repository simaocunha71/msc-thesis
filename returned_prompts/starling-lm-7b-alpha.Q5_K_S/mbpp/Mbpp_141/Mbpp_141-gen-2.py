"""
def pancake_sort(nums):
    while len(nums) > 1:
        max_num = max(nums[:-1])
        idx = nums.index(max_num)
        nums.insert(0, nums.pop(idx+1))
    return nums

def test_pancake_sort():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    print("All Tests Passed")

if __name__ == "__main__":
    test_pancake_sort()
"""

def pancake_sort(nums):
    while len(nums) > 1:
        max_num = max(nums[:-1])
        idx = nums.index(max_num)
        nums.insert(0, nums.pop(idx))
    return nums

def test_pancake_sort():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    print("All Tests Passed")

if __name__ == "__main__":
    test_pancake_sort()




"""
def pancake_sort(nums):
    while len(nums) > 1:
        max_num = max(nums[:-1])
        idx = nums.index(max_num)
        nums.insert(0, nums.pop(idx))
    return nums

def test_pancake_sort():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    print("All Tests Passed")

if __name__ == "__main__":
    test_pancake_sort()
"""

"""
def pancake_sort(nums):
