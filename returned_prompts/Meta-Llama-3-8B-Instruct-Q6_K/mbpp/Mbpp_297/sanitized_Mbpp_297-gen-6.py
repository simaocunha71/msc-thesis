def flatten_list(input_list):
    if isinstance(input_list, list):
        output_list = []
        for item in input_list:
            output_list += flatten_list(item)
        return output_list
    else:
        return [input_list]  # single element, not a list