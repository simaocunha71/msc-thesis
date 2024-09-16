def count_Occurrence(tup_list,list_to_count):
    count=0
    for i in list_to_count:
        count += tup_list.count(i)
    return count