def two_unique_nums(*args):
    unique_nums = set()
    for lst in args:
        for num in lst:
            unique_nums.add(num)
    return list(unique_nums)