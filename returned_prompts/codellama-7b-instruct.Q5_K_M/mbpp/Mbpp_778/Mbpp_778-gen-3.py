def pack_consecutive_duplicates(my_list):
    return [[my_list[i]] + [my_list[j]] for i in range(len(my_list)) for j in range(i+1, len(my_list)) if my_list[i] == my_list[j]]



