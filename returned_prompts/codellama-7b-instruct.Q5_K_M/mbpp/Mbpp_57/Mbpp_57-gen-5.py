def find_Max_Num(my_list):
    my_list.sort(reverse=True)
    largest_num = ""
    for digit in my_list:
        largest_num += str(digit)
    return int(largest_num)
