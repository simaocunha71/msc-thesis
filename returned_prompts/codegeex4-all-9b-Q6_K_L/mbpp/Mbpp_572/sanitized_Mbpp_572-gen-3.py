def two_unique_nums(*lists):
    unique_nums = set()
    for lst in lists:
        for num in lst:
            if num not in unique_nums:
                unique_nums.add(num)
    return list(unique_nums)