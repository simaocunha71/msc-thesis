def max_length(lists):
    max_len = 0
    max_list = []
    for i in lists:
        if(len(i) > max_len):
            max_len = len(i)
            max_list = i
    return (max_len, max_list)