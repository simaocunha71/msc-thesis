def Find_Min(input_list):
    length = 999999999
    for sublist in input_list:
        if len(sublist) < length:
            length = len(sublist)
    return length