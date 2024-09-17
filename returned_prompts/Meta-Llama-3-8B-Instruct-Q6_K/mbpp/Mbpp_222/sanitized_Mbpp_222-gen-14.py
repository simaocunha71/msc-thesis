def check_type(t):
    first_element = type(t[0])
    for element in t:
        if type(element) != first_element:
            return False
    return True