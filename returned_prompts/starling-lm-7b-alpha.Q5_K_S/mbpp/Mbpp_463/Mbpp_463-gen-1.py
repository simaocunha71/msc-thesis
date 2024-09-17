
def max_subarray_product(nums: list) -> int:
    max_product = float('-inf')
    curr_product = 1
    for num in nums:
        curr_product = max(curr_product * num, 1)
        max_product = max(max_product, curr_product)
    return max_product


