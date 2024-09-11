"""
def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = float('inf')

    for num in nums:
        max_product, min_product = max(max_product * num, min_product * num, num), min(max_product * num, min_product * num, num)
        max_product = max(max_product, min_product)

    return max_product
"""

def max_subarray_product(nums):
    max_product = min_product = num = 1
    for i in range(len(nums)):
        num = max(num, nums[i])
        max_product = max(max_product, num * min_product)
        min_product = min(min_product, nums[i])
    return max_product

def test():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([-2, -3, -4]) == -2
    assert max_subarray_product([-2, -3, -4, 1]) == 1
    assert max_subarray_product([-2, 1]) == 1
    assert max_subarray_product([-2]) == -2
    print("All tests passed.")

test()














"""

def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = float('inf')

    for num in nums:
        max_product, min_product = max(max_product * num, min_product * num, num), min(max_product * num, min_product * num, num)
        max_product = max(max_product, min_product)

    return max_product

def test():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([-