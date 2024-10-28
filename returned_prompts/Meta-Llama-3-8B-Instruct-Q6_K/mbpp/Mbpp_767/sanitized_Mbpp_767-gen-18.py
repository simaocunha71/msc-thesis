def get_pairs_count(lst, sum):
    freq = {}
    count = 0
    for num in lst:
        if sum - num in freq:
            count += freq[sum - num]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count