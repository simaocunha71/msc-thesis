def Find_Max(lst):
    max_length = 0
    max_element = None
    for element in lst:
        if len(element) > max_length:
            max_length = len(element)
            max_element = element
    return max_element

