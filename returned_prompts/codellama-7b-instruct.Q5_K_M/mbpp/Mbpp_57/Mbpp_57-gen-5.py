
def find_Max_Num(my_list):
    max_num = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            for k in range(j+1, len(my_list)):
                num = my_list[i] * 100 + my_list[j] * 10 + my_list[k]
                if num > max_num:
                    max_num = num
    return max_num


