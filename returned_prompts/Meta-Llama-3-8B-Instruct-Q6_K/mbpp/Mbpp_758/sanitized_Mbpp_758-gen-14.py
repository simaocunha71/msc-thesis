def unique_sublists(lst):
    count_dict = {}
    for item in lst:
        item_tuple = tuple(item)
        if item_tuple in count_dict:
            count_dict[item_tuple] += 1
        else:
            count_dict[item_tuple] = 1
    return count_dict