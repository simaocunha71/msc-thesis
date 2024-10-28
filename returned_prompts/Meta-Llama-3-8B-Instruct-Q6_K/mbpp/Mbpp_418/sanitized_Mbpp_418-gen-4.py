def Find_Max(lst):
    max_length = max(len(i) for i in lst)
    return max([i for i in lst if len(i) == max_length], key = len)  # Return the list with maximum length. 