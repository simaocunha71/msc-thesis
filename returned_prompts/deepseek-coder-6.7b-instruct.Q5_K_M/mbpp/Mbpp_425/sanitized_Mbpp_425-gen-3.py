def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if type(sublist) == list:
            if element in sublist:
                count += 1
        else:
            continue
    return count