
def max_length(lst):
    max_len = len(max(lst, key=len))
    max_lst = [i for i in lst if len(i) == max_len]
    return max_len, max_lst[0]


