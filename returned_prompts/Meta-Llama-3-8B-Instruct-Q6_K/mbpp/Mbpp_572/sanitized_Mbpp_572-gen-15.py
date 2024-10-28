def two_unique_nums(lst):
    num_count = {}
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    return [num for num, count in num_count.items() if count == 1]