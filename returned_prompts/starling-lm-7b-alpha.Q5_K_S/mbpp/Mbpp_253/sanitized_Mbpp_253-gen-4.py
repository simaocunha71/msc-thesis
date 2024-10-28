def count_integer(input_list):
    result = 0
    for element in input_list:
        if isinstance(element, int):
            result += 1
    return result