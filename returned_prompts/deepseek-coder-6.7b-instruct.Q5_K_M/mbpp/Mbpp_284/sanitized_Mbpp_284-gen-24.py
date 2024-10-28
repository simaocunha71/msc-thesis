def check_element(lst, elem):
    return all(elem == lst[i] for i in range(len(lst)))