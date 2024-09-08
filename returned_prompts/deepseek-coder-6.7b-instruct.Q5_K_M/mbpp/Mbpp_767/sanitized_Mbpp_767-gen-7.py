def get_pairs_count(lst, _sum):
    n = len(lst)
    m = {}
    twice_count = 0

    # count occurrences of all elements
    for i in range(n):
        if lst[i] in m:
            m[lst[i]] += 1
        else:
            m[lst[i]] = 1

    # iterate through each element and increment the count (to handle cases when sum is 0)
    for i in range(n):
        if (_sum - lst[i]) in m:
            twice_count += m[_sum - lst[i]]

        # if sum is 0, then count pairs (a,a) only if a occurs more than once
        if _sum == 0:
            twice_count -= 1

    # return half of twice_count as pairs are counted twice
    return twice_count // 2