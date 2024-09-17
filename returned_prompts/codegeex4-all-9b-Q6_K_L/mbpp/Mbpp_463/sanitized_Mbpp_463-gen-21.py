def max_subarray_product(nums):
    if not nums:
        return 0

    max_product = float('-inf')
    current_max = 1
    current_min = 1

    for num in nums:
        if num == 0:
            current_max = 1
            current_min = 1
            continue

        temp = current_max
        current_max = max(num, current_max * num, current_min * num)
        current_min = min(num, temp * num, current_min * num)

        max_product = max(max_product, current_max)

    return max_product