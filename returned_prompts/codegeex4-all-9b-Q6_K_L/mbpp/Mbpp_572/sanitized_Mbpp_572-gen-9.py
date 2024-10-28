def two_unique_nums(*lists):
    unique_nums = []
    for lst in lists:
        for num in lst:
            if num not in unique_nums:
                unique_nums.append(num)
    return unique_nums