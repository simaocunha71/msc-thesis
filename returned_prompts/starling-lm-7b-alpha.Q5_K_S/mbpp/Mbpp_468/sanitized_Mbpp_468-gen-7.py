def max_product(nums):
    best_product = 1
    cur_product = 1
    for i in nums:
        cur_product = max(cur_product * i, i)
        best_product = max(best_product, cur_product)
    return best_product