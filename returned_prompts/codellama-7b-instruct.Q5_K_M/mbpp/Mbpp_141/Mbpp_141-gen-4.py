
def pancake_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    for i in range(len(my_list) - 1, 0, -1):
        if my_list[i] == my_list[0]:
            my_list = my_list[:i] + my_list[i + 1:]
        else:
            my_list[0], my_list[i] = my_list[i], my_list[0]
            break
    return my_list


