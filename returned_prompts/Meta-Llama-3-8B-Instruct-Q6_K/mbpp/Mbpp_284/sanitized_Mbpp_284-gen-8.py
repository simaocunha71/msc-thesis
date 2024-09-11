def check_element(lst, element):
    return all(x == element for x in lst) if len(lst) > 0 else False