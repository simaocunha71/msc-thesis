def get_pairs_count(lst, sum):
    count = 0
    seen = {}
    for num in lst:
        complement = sum - num
        if complement in seen:
            count += seen[complement]
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    return count