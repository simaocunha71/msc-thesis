def max_length(lst):
    max_len = max(len(lst[i]) for i in range(len(lst)))
    for i in lst:
        if len(i) == max_len:
            return max_len, i