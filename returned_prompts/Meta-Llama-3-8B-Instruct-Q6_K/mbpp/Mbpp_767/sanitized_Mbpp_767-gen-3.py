def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count