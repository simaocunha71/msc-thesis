def max_subarray_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    # 1. find the max product of a subarray
    # 2. find the max product of a subarray with the first element
    # 3. find the max product of a subarray with the last element

    max_product_subarray = max(nums)
    max_product_first = max(nums)
    max_product_last = max(nums)

    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            product = nums[i] * nums[j]
            if product > max_product_subarray:
                max_product_subarray = product

            if i == 0 and product > max_product_first:
                max_product_first = product

            if j == len(nums) - 1 and product > max_product_last:
                max_product_last = product

    return max(max_product_subarray, max_product_first, max_product_last)

