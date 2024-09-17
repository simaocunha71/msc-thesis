def get_pairs_count(nums: list, sum_: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == sum_:
                count += 1
    return count