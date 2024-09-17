def combinations_list(lst):
    ans = [[]]
    for elem in lst:
        ans += [comb + [elem] for comb in ans]
    return ans