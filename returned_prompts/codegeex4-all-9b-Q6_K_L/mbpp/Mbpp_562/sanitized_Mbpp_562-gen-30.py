def Find_Max_Length(test_list):
    max_len = 0
    for i in test_list:
        max_len = max(max_len, len(i))
    return max_len