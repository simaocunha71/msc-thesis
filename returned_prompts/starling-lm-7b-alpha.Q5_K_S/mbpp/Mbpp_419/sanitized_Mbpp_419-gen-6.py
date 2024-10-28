def round_and_sum(nums):
    rounded_nums = [round(num) for num in nums]
    total_sum = sum(rounded_nums)
    length = len(nums)
    result = total_sum * length
    return result