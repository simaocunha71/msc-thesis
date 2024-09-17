def max_length(lst: list):
    max_len = 0
    max_list = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_list = i
    return (max_len, max_list)