def get_pairs_count(lst, sum_val):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum_val:
                count += 1
    return count