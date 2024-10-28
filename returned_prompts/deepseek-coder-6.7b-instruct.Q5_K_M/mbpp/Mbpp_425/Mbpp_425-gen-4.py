
def count_element_in_list(lst, x):
    return sum(1 for sub in lst for el in sub if el == x)


