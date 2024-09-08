def two_unique_nums(*lists):
    unique_nums = set()
    for lst in lists:
        for num in lst:
            unique_nums.add(num)
    return list(unique_nums)