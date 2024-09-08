def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if type(sublist) is list:
            count += sublist.count(element)
        else:
            if sublist == element:
                count += 1
    return count