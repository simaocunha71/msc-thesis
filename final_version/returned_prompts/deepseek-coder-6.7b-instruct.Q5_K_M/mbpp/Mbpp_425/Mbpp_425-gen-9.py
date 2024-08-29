def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(element)
        else:
            if sublist == element:
                count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [