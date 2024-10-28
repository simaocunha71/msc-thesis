def find_Max_Num(my_list):
    max_num = -1
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            num = int(my_list[i] + my_list[j])
            if num > max_num:
                max_num = num
    return max_num