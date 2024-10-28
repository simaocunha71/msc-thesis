def find_sum(list):
    non_repeated_list = []
    for i in list:
        if list.count(i) == 1:
            non_repeated_list.append(i)
    return sum(non_repeated_list)