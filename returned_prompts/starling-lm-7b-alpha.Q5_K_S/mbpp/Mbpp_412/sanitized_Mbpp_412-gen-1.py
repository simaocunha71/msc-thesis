def remove_odd(input_list):
    output_list = []
    for i in input_list:
        if i % 2 == 0:
            output_list.append(i)
    return output_list