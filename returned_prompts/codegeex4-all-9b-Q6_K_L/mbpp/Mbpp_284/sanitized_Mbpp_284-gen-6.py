def check_element(lst, element):
    for item in lst:
        if item != element:
            return False
    return True