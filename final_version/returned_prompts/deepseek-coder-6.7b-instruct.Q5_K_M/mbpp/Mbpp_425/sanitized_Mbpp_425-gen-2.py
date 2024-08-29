def count_element_in_list(lst, ele):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(ele)
        else:
            if sublist == ele:
                count += 1
    return count