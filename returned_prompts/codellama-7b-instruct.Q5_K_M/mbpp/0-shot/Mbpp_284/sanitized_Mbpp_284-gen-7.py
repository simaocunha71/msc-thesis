def check_element(my_list, element):
    if len(my_list) == 0:
        return False
    else:
        return all(x == element for x in my_list)