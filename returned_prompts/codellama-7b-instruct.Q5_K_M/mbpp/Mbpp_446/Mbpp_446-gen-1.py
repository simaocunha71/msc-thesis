def count_Occurrence(my_list, my_tuple):
    count = 0
    for i in my_list:
        if i in my_tuple:
            count += my_list.count(i)
    return count


