def find_sum(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    non_repeated = [num for num, count in counts.items() if count == 1]
    return sum(non_repeated)