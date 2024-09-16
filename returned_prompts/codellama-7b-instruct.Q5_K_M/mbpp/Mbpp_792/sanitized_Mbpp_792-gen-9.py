def count_list(my_list):
    count = 0
    for item in my_list:
        if type(item) == list:
            count += 1
    return count