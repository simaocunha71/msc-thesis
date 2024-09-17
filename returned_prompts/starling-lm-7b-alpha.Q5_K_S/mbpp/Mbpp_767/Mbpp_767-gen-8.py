
def get_pairs_count(nums: list, sum: int) -> int:
    d = {}
    for i in nums:
        if sum - i in d:
            d[sum-i] += 1
        else:
            d[sum-i] = 1
    return sum(d.values())


