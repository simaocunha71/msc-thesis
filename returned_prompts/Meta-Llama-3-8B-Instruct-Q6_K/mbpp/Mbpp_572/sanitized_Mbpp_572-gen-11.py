def two_unique_nums(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return [num for num, freq in count.items() if freq == 1]