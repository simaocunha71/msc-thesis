def _index(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
    return index

def test_index():
    assert _index([1, 2, 3], 3) == 2

test_index()

"""
Write a