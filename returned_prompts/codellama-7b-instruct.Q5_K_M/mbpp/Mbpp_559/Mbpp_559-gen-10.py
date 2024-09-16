def max_sub_array_sum(lst, k=0):
    if not lst:
        return k
    m = max(lst)
    return max(max_sub_array_sum(lst[1:], m), max_sub_array_sum(lst[1:], k + m))
