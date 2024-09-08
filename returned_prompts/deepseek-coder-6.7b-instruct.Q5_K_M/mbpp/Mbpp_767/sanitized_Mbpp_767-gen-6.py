def get_pairs_count(lst, sum):
    lst.sort()
    cnt, i, j = 0, 0, len(lst) - 1
    while i < j:
        if lst[i] + lst[j] == sum:
            cnt += 1
            i += 1
            j -= 1
        elif lst[i] + lst[j] < sum:
            i += 1
        else:
            j -= 1
    return cnt