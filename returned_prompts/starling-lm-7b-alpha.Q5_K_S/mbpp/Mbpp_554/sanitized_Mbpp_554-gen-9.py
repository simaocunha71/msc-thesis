def Split(input_list):
    output_list = []
    for i in input_list:
        if i % 2 == 1:
            output_list.append(i)
    return output_list