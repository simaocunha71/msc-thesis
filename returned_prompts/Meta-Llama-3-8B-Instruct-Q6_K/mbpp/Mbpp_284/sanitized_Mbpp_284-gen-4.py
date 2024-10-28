def check_element(lst, element):
    return all(i == element for i in lst)  # or return lst.count(element) == len(lst)  # or return len(set(lst)) == 1 and lst[0] == element