def two_unique_nums(lists):
    unique_nums = set()
    for lst in lists:
        unique_nums.update(lst)
    return list(unique_nums)