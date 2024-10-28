def two_unique_nums(lst):
    unique_nums = set()
    for num in lst:
        if num not in unique_nums:
            unique_nums.add(num)
    return list(unique_nums)  # or sorted(list(unique_nums)) for sorted output