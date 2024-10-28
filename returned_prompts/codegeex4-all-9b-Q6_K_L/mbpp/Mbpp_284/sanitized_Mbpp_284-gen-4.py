def check_element(lst, element):
    for i in lst:
        if i != element:
            return False
    return True