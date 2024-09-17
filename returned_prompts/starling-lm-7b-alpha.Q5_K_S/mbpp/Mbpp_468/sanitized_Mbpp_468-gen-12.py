def max_product(nums: list) -> int:
    max_product = 1
    current_max = 0
    for num in nums:
        if num > current_max:
            max_product *= num
            current_max = num
    return max_product