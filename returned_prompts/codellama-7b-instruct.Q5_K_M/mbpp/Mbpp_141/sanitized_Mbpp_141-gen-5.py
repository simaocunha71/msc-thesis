def pancake_sort(my_list):
    for length in range(len(my_list), 0, -1):
        for i in range(length):
            if my_list[i] == length:
                my_list = my_list[0:i] + my_list[i+1:length] + [my_list[i]]
                break
    return my_list