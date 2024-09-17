def sum_negativenum(nums: list) -> int:
    sum_neg_nums = sum(num for num in nums if num < 0)
    return sum_neg_nums

