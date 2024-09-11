def Find_Max(list):
    max_length = 0
    max_element = None
    for element in list:
        if len(element) > max_length:
            max_length = len(element)
            max_element = element
    return max_element