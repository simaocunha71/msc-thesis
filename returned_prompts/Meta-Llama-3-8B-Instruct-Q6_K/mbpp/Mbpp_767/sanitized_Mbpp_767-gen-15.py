def get_pairs_count(lst, sum):
    pairs_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                pairs_count += 1
    return pairs_count