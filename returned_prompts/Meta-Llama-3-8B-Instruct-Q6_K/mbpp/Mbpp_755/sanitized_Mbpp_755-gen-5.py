def second_smallest(nums):
    if len(set(nums)) < 2:
        return None
    return sorted(set(nums))[1] if sorted(set(nums))[0] != min(nums) else min([x for x in nums if x > min(nums)]) if len([x for x in nums if x > min(nums)]) > 0 else None