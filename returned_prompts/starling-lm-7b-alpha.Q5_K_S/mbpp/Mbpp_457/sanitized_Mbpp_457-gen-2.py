def Find_Min(list):
    min_length = len(list[0])
    min_list = list[0]
    for i in range(len(list)):
        if len(list[i]) < min_length:
            min_length = len(list[i])
            min_list = list[i]
    return min_list