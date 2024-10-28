def insert_element(lst, ele):
    lst = [ele] + lst
    new_lst = []
    for i in lst:
        new_lst.append(i)
        new_lst.append(ele)
    return new_lst

