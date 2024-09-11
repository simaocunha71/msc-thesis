def second_smallest(nums):
    return sorted(set(nums))[1] if len(set(nums)) > 1 else None