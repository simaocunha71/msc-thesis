def check_element(lst, element):
    return all(x == element for x in lst)  # or return len(set(lst)) == 1 and lst[0] == element