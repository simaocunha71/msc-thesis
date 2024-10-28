def check_element(my_list,element):
    if all(item==element for item in my_list):
        return True
    else:
        return False
