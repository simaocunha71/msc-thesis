
def test_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

print(test_duplicate([1,2,3,4,5])) # False


