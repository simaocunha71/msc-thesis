def consecutive_duplicates(my_list):
    return [my_list[i] for i in range(len(my_list)) if i == 0 or my_list[i] != my_list[i-1]]


