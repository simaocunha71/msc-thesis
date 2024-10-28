def pack_consecutive_duplicates(my_list):
    return [[my_list[i], my_list[i+1]] for i in range(len(my_list)-1) if my_list[i]==my_list[i+1]]