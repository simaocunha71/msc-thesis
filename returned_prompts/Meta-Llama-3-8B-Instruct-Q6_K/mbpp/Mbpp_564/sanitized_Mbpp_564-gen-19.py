def count_Pairs(lst, k):
    count = 0
    seen = set()
    for num in lst:
        for other in seen:
            if num != other and num <= k:
                count += 1
        seen.add(num)
    return count