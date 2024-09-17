def get_pairs_count(lst, sum):
    count = 0
    counts = {}
    for num in lst:
        if sum - num in counts:
            count += counts[sum - num]
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return count