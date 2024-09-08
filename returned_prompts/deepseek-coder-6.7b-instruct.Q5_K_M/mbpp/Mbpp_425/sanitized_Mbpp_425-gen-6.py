def count_element_in_list(lst,ele):
    count = 0
    for sublist in lst:
        if type(sublist) == list:
            count += sublist.count(ele)
    return count