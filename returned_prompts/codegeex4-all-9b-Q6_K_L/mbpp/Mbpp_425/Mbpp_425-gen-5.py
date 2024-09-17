def count_element_in_list(lst, target):
    return sum(1 for sublist in lst for item in sublist if item == target)

