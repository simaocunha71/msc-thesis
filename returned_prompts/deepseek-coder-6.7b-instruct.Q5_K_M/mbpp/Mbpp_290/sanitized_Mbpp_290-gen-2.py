def max_length(lst):
    max_len = max(len(lst[i]) for i in range(len(lst)))
    max_lst = [lst[i] for i in range(len(lst)) if len(lst[i]) == max_len]
    return max_len, max_lst[0]