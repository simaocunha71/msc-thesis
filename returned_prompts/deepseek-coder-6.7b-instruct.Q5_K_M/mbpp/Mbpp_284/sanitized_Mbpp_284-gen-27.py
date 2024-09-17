def check_element(lst,elm):
    return all(elm == lst[i] for i in range(len(lst)))