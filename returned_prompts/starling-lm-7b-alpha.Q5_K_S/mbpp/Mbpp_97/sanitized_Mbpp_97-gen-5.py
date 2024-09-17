def frequency_lists(list_of_lists):
    output_dict = {}
    for sublist in list_of_lists:
        for element in sublist:
            if element in output_dict:
                output_dict[element] += 1
            else:
                output_dict[element] = 1
    return output_dict