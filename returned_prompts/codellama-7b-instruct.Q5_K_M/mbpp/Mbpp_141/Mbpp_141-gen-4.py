def pancake_sort(my_list):
    def flip(i):
        my_list[:i+1] = my_list[:i+1][::-1]
    for i in range(len(my_list)-1, -1, -1):
        if my_list[i] > my_list[0]:
            flip(i)
    return my_list
