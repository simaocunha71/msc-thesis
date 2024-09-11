def insert_element(lst, element):
    return [element] + [element if i == 0 else x for i, x in enumerate(lst)] + [element]