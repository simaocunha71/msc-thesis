def max_length(input_list):
    max_length = 0
    max_list = []
    for i in input_list:
        if len(i) > max_length:
            max_length = len(i)
            max_list = i
    return max_length, max_list