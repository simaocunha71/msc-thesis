def round_and_sum(nums: list):
    rounded_nums = [round(num) for num in nums]
    total_sum = sum(rounded_nums)
    result = total_sum * len(rounded_nums)
    return result