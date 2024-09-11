def check_element(lst, element):
    return all(item == element for item in lst)  # or return len(set(lst)) == 1 and lst[0] == element