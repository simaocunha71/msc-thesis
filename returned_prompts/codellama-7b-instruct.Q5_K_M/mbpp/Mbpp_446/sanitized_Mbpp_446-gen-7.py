def count_Occurrence(my_list, ele_list):
    count = 0
    for i in my_list:
        if i in ele_list:
            count += 1
    return count