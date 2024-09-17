
def Find_Max(my_list):
    max_length = 0
    max_element = None
    for element in my_list:
        if len(element) > max_length:
            max_length = len(element)
            max_element = element
    return max_element


