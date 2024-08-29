def round_and_sum(nums):
    rounded = [round(n) for n in nums]
    return sum(rounded) * len(rounded)