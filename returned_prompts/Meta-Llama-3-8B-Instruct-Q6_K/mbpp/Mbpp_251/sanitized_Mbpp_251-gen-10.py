def insert_element(lst, elem):
    new_lst = [elem]
    new_lst.extend([elem] + lst)
    return new_lst