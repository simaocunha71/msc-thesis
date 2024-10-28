    unique_nums = list(set(lst))
    unique_nums.sort()
    return unique_nums[1] if len(unique_nums) > 1 else None


