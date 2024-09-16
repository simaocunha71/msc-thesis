def count_Occurrence(my_list, tuple_list):
    count = 0
    for i in my_list:
        if i in tuple_list:
            count = count + 1
    return count
