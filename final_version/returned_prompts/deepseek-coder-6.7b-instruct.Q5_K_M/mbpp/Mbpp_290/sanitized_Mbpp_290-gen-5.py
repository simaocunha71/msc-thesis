def max_length(lst):
    max_len = len(max(lst, key=len))
    max_lst = [lst[i] for i in range(len(lst)) if len(lst[i]) == max_len]
    return max_len, max_lst