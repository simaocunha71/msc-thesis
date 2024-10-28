def max_length(test_list):
    max_len = max(len(lst) for lst in test_list)
    max_list = [lst for lst in test_list if len(lst) == max_len]
    return max_len, max_list

