
def Find_Max(test_list):
    max_len = 0
    max_val = None
    for i in test_list:
        if len(i) > max_len:
            max_len = len(i)
            max_val = i
    return max_val


