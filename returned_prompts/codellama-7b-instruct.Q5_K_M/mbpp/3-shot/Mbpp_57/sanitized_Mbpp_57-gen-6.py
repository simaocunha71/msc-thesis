def find_Max_Num(my_list):
    max_num = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            current_num = my_list[i] * 10 + my_list[j]
            if current_num > max_num:
                max_num = current_num
    return max_num