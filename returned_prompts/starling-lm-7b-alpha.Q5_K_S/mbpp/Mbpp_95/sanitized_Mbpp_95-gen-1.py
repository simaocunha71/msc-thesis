def Find_Min_Length(input_list):
    min_len = len(input_list[0])
    for i in range(len(input_list)):
        if len(input_list[i]) < min_len:
            min_len = len(input_list[i])
    return min_len