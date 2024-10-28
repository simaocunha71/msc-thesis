def max_product(nums):
    max_product = 1
    min_product = 1
    result = 1
    for num in nums:
        if num < 0:
            max_product, min_product = min_product, max_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        result = max(result, max_product)
    return result