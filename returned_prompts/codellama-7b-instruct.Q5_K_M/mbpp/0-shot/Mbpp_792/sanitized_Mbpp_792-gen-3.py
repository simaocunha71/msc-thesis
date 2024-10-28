def count_list(my_list):
    count = 0
    for sublist in my_list:
        if isinstance(sublist, list):
            count += 1
            count += count_list(sublist)
    return count