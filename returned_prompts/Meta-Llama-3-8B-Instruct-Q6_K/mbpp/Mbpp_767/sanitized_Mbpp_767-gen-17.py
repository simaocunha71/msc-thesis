def get_pairs_count(lst, sum):
    count = 0
    seen = set()
    for num in lst:
        complement = sum - num
        if complement in seen:
            count += 1
        seen.add(num)
    return count