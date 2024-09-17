def two_unique_nums(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return [num for num, count in counts.items() if count == 1]