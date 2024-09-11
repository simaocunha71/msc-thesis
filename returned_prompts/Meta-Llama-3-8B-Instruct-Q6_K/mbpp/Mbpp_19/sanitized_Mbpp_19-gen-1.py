def test_duplicate(nums):
    return len(nums) != len(set(nums))  # Check if the length of the array is not equal to the length of its set, which means there are duplicate elements. 