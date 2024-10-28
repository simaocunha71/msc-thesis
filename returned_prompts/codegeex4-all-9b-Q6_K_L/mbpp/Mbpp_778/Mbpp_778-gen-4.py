def pack_consecutive_duplicates(nums: list) -> list:
    return [[num] * count for num, count in groupby(nums)]

